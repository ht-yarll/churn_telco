-- Desafio 2: Média de pagamento do internetservice
SELECT
	ROUND(AVG(monthlycharges::DECIMAL), 2) AS avg_monthly_charges,
	internetservice AS internet_service
FROM churn_telco.tb_wa_fn_usec__telco_customer_churn
GROUP BY internetservice 
ORDER BY avg_monthly_charges DESC