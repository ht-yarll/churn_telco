from churn_telco.interfaces.load_strategy_interface import LoadDataStrategy
from churn_telco.interfaces.extract_strategy_interface import ExtractDataStrategy
from churn_telco.interfaces.transform_strategy_interface import TransformDataStrategy

class ETLPostgresContext:
    def __init__(self, extractor: ExtractDataStrategy, transformer: TransformDataStrategy, loader: LoadDataStrategy):
        self.extractor = extractor
        self.transform = transformer
        self.load = loader

    def run(self):
        try:
            dfs = self.extractor.extract()
            for filename, df in dfs:
                transformed = self.transform.transform(df, filename)
                self.load.load()
        except Exception as e:
            print(f"❌ Error while running ETL context: {e}")
