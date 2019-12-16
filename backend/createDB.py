from sqlitedict import SqliteDict

userCredentials = SqliteDict("userCredentialsDB.sqlite", autocommit=True)
trashData = SqliteDict("trashDataDB.sqlite",  autocommit=True)

userCredentials["Sebastian"] = "password"
userCredentials["Admin"] = "Admin"
trashData["Sebastian"] = {"plastic": 5, "paper": 7, "rest": 12}

userCredentials.close()
trashData.close()
