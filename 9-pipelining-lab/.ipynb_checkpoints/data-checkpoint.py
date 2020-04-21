import numpy as np
is_manhattan = (np.where(pruned_df.borough == 'Manhattan', 1, 0))
pruned_df.loc[:, :]['is_manhattan'] = is_manhattan

updated_df = pd.concat([pruned_df, pd.get_dummies(pruned_df.is_manhattan)], axis=1)
updated_df = updated_df.dropna(subset=['average_score_sat_math'])
updated_df.columns = ['borough', 'average_score_sat_math', 'is_manhattan', 'outside_manhattan', 'inside_manhattan']