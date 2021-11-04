# https://medium.com/analytics-vidhya/fetch-data-from-kaggle-with-python-9154a4c610e3

from kaggle.api.kaggle_api_extended import KaggleApi

if __name__ == '__main__':
    print("Kaggle Data Extractor\n")

    PathForDownload = "C:\\Users\\y84201228\\PycharmProjects\\KaggleExtractor\\Dataset_Folder"

    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files('kannan1314/innocent-deaths-caused-by-police-all-time', path=PathForDownload, unzip=True)

