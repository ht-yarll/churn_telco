--Desafio 3: 3 maiores método de pagamento associado a churn
SELECT 
	paymentmethod AS payment_method,
	count(*) AS churned_customers
FROM churn_telco.tb_wa_fn_usec__telco_customer_churn
WHERE churn = 'Yes'
GROUP BY payment_method 
ORDER BY churned_customers DESC
LIMIT 3