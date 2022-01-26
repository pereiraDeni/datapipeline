from aws_cdk import core
from dataplatform.data_lake.stack import DataLakeStack

app = core.App()
data_lake = DataLakeStack(app)
app.synth()