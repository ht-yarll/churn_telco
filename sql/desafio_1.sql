-- Desafio 1: perfil dos clientes que cancelaram
SELECT
	COUNT(*) AS qtn_churn,
	gender,
	contract
FROM churn_telco.tb_wa_fn_usec__telco_customer_churn
WHERE churn = 'Yes'
GROUP BY gender, contract
ORDER BY qtn_churn DESC