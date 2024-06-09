import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

def handle_missing_values(df):
    df = df.copy()
    df['Item_Weight'] = df['Item_Weight'].fillna(df['Item_Weight'].mean())
    df['Item_Weight'] = df.groupby('Item_Type')['Item_Weight'].transform(lambda x: x.fillna(x.mean()))
    df['Outlet_Size'] = df.groupby('Outlet_Type')['Outlet_Size'].transform(lambda x: x.fillna(x.mode()[0] if not x.mode().empty else 'Unknown'))
    return df

@dataclass
class DataTransformConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformConfig()

    def get_data_transformer_obj(self):
        try:
            categorical_cols = ['Item_Fat_Content', 'Item_Type', 'Outlet_Identifier',
                                'Outlet_Size', 'Outlet_Location_Type', 'Outlet_Type']
            numerical_cols = ['Item_Weight', 'Item_Visibility', 'Item_MRP', 'Outlet_Establishment_Year']

            num_pipeline = Pipeline(
                steps=[
                    ('scaler', StandardScaler()),
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ('onehot', OneHotEncoder(handle_unknown='ignore')),
                ]
            )

            logging.info("The dataset has undergone all the transformation and preprocessing for both numerical and categorical values")

            preprocessor = ColumnTransformer(
                [
                    ('num_pipeline', num_pipeline, numerical_cols),
                    ('cat_pipeline', cat_pipeline, categorical_cols)
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transform(self, train_path, test_path):
        try:
            # Ensure the artifacts directory exists
            artifacts_dir = 'artifacts'
            if not os.path.exists(artifacts_dir):
                os.makedirs(artifacts_dir, exist_ok=True)
            
            train_df = pd.read_csv(train_path)
            train_df = handle_missing_values(train_df)
            test_df = pd.read_csv(test_path)
            test_df = handle_missing_values(test_df)
            logging.info("The dataset has been read for preprocessing")

            logging.info("Obtaining the preprocessing object")
            preprocessing_obj_tr = self.get_data_transformer_obj()

            target_column_name = 'Item_Outlet_Sales'
            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info("Applying preprocessing object on training and testing dataframes")

            input_feature_train_arr=preprocessing_obj_tr.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj_tr.transform(input_feature_test_df)
            
            
            # Convert sparse matrices to dense matrices if needed
            if isinstance(input_feature_train_arr, np.ndarray):
                input_feature_train_arr_dense = input_feature_train_arr
            else:
                input_feature_train_arr_dense = input_feature_train_arr.toarray()

            if isinstance(input_feature_test_arr, np.ndarray):
                input_feature_test_arr_dense = input_feature_test_arr
            else:
                input_feature_test_arr_dense = input_feature_test_arr.toarray()

            # Reshape the target arrays to ensure they have a shape of (n_samples, 1)
            target_feature_train_arr = target_feature_train_df.values.reshape(-1, 1)
            target_feature_test_arr = target_feature_test_df.values.reshape(-1, 1)

            train_arr = np.hstack((input_feature_train_arr_dense, target_feature_train_arr))
            test_arr = np.hstack((input_feature_test_arr_dense, target_feature_test_arr))


            logging.info("Saved Preprocessing object")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj_tr
            )
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        except Exception as e:
            raise CustomException(e, sys)

