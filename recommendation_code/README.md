# Data:
- 1.3M Users
- 106K Items
- 31.8M Transaction records

# For existing Users (Implicit_ALS.ipynb):
- Use ALS for training
- Tune the hyperparameters
- Got the recommendations based on the past transaction records for each user

# For new Users (Recommend.ipynb):
- Use user-based filtering 
- Clod start with some features and preferences of users
- Got the recommendations based on the existing users who have the highest similarity
