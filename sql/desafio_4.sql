-- Desafio 4: Tempo médio de permanência com ou sem proteção de dispositivo
SELECT
	ROUND(AVG(tenure::decimal), 2) AS avg_tenure,
	deviceprotection AS device_protection
FROM churn_telco.tb_wa_fn_usec__telco_customer_churn
GROUP BY device_protection 
ORDER BY avg_tenure DESC