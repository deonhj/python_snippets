m = nutrition['vitamin_c_mg'].mean()
mp2sd = m + nutrition.vitamin_c_mg.std() * 2
mp3sd = m + nutrition.vitamin_c_mg.std() * 3
result_set = nutrition[nutrition.vitamin_c_mg.between(mp2sd, mp3sd)]