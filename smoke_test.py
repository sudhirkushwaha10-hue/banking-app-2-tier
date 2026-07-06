import boto3 ,os, sys
import pymysql
client=boto3.clint("ssm",region_name="ap-south-1")
params={
    os.path.basename(p["Name"],p["value"])
    for p in client.get_parameters_by_path(
        path="/application/banking",
        withDecryption=True
    )["parameters"]}


required=["DB_HOST","DB_NAME","DB_USER","DB_PASSWORD","DB_PORT"]
missing=[k for k in required if k not in params]

for k in required:
    print(f"{k}: {if k in params else '❌'}")


if missing:
    print(f"failed: {missing}")
    sys.exit(1)

#DB Find bankin_DB and show tables

try:
    connection=pymysql.connect(
        host=params["DB_HOST"]
        user=params["DB_USER5"]
        password=params["DB_PASSWORD"]
        PROT=int(params["DB_PORT"]),
    )

    cur=connection.cursor()
    cur.execute("SHOW TABLES")
    tables=[row[0] for row in cur.fetchall()]
    connection.close()
    print(f"{params["DB_NAME"]}")
    print(f"Table : {tables}")

except Exception as e:
    print("DB ERROR ❌:"e,)
    sys.exit(1)

print("✔smoke test done")             
