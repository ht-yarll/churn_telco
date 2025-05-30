from churn_telco.utils.config import load_config
from churn_telco.strategy.ExtractCSVLocalStrategy import ExtractFromLocalCSV
from churn_telco.strategy.TransformCSVLocalStrategy import TransformCSVDataLocal
from churn_telco.strategy.LoadToPostgresStrategy import LoadDataPostgres
from churn_telco.context.etl_context import ETLPostgresContext

def main():
    try:
        config = load_config()
        context = ETLPostgresContext(
            extractor= ExtractFromLocalCSV(config),
            transformer = TransformCSVDataLocal(config),
            loader = LoadDataPostgres(config)
            )

        context.run()
        return '🎉 Success 🎉'
    
    except Exception as e:
        print(f'😞 Failed to run app: {e}"')
        return None

if __name__ == '__main__':
    main()