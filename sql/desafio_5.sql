-- Desafio 5: Como o tempo de permanência varia entre diferentes combinações de serviços contratados
-- Com Churn
SELECT
	ROUND(AVG(tenure::decimal), 2) AS avg_tenure,
	techsupport AS tech_supp,
	streamingmovies  AS streaming_movies,
	streamingtv  AS streaming_tv,
	internetservice  AS internet_service
FROM churn_telco.tb_wa_fn_usec__telco_customer_churn
WHERE churn = 'Yes'
GROUP BY tech_supp, streaming_movies, streaming_tv, internet_service 
ORDER BY avg_tenure DESC

-- Sem Churn
SELECT
	ROUND(AVG(tenure::decimal), 2) AS avg_tenure,
	techsupport AS tech_supp,
	streamingmovies  AS streaming_movies,
	streamingtv  AS streaming_tv,
	internetservice  AS internet_service
FROM churn_telco.tb_wa_fn_usec__telco_customer_churn
WHERE churn = 'No'
GROUP BY tech_supp, streaming_movies, streaming_tv, internet_service 
ORDER BY avg_tenure DESC