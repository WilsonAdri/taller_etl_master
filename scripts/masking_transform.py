import json
from pyspark.sql import DataFrame
from pyspark.sql.functions import col, expr

def load_masking_rules(config_path: str = "config/masking_rules.json"):
    with open(config_path, 'r') as f:
        return json.load(f)

def apply_masking(df: DataFrame, rules_config: dict) -> DataFrame:
    """Aplicar reglas de enmascaramiento dinámicas"""
    
    fields = rules_config.get("fields", {})
    df_masked = df

    for field, rule in fields.items():
        if field not in df.columns:
            continue

        rule_type = rule.get("type")
        params = rule.get("params", {})

        # 🔐 1. STRING (transaction_id)
        if rule_type == "mask_string":
            visible = params.get("visible_digits", 4)
            mask_char = params.get("mask_char", "*")

            expr_mask = f"""
                CASE 
                    WHEN {field} IS NULL THEN NULL
                    ELSE CONCAT(
                        REPEAT('{mask_char}', LENGTH(CAST({field} AS STRING)) - {visible}),
                        RIGHT(CAST({field} AS STRING), {visible})
                    )
                END
            """
            df_masked = df_masked.withColumn(field, expr(expr_mask))

        # 🔢 2. INTEGER (user_id)
        elif rule_type == "mask_integer":
            visible = params.get("visible_digits", 2)

            expr_mask = f"""
                CASE 
                    WHEN {field} IS NULL THEN NULL
                    ELSE CAST(
                        CONCAT(
                            REPEAT('0', LENGTH(CAST({field} AS STRING)) - {visible}),
                            RIGHT(CAST({field} AS STRING), {visible})
                        ) AS INT
                    )
                END
            """
            df_masked = df_masked.withColumn(field, expr(expr_mask))

        # 💰 3. NUMERIC (amount)
        elif rule_type == "mask_numeric":
            method = params.get("method", "round")
            precision = params.get("precision", 0)

            if method == "round":
                df_masked = df_masked.withColumn(field, expr(f"ROUND({field}, {precision})"))
            elif method == "zero":
                df_masked = df_masked.withColumn(field, expr(f"CAST(0 AS DOUBLE)"))
            elif method == "null":
                df_masked = df_masked.withColumn(field, expr("NULL"))
        
        else:
            print(f"Regla de enmascaramiento no reconocida: {rule_type}")

    return df_masked