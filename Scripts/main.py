import joblib
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import llm
import warnings
import alert
warnings.filterwarnings("ignore")

svm = joblib.load(r"E:\NIDS_FINAL\Saved\svc_model.joblib")
rf = joblib.load(r"E:\NIDS_FINAL\Saved\rf_model.joblib")
ensemble = joblib.load(r"E:\NIDS_FINAL\Saved\Ensemble.joblib")

le = LabelEncoder()


def predict(packet):
    packet = packet.reshape(1, -1)
    svm.predict(packet)
    rf.predict(packet)
    result = ensemble.predict(packet)
    result = le.inverse_transform(result)
    return result


df = pd.read_csv(r"E:\NIDS_FINAL\Data\dataset\KDDTest+.txt")

columns = (['duration','protocol_type','service','flag','src_bytes','dst_bytes','land','wrong_fragment','urgent','hot'
    ,'num_failed_logins','logged_in','num_compromised','root_shell','su_attempted','num_root','num_file_creations'
    ,'num_shells','num_access_files','num_outbound_cmds','is_host_login','is_guest_login','count','srv_count','serror_rate'
    ,'srv_serror_rate','rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate','srv_diff_host_rate','dst_host_count','dst_host_srv_count'
    ,'dst_host_same_srv_rate','dst_host_diff_srv_rate','dst_host_same_src_port_rate','dst_host_srv_diff_host_rate','dst_host_serror_rate'
    ,'dst_host_srv_serror_rate','dst_host_rerror_rate','dst_host_srv_rerror_rate','attack','level'])

df.columns=columns

list = ['land',
        'num_compromised',
        'root_shell',
        'num_file_creations',
        'num_shells',
        'diff_srv_rate',
        'srv_diff_host_rate',
        'dst_host_same_srv_rate',
        'dst_host_srv_rerror_rate']


for col in df.select_dtypes(include='object'):
    df[col] = le.fit_transform(df[col])

print(df)
packet1 = []
for i in list :
    packet1.append(df[i])

new_df = pd.DataFrame(packet1)
new_df = new_df.T
ans = predict(new_df.loc[10].values)

if ans == "Normal":
    print("Normal")
else:
    lm_output = llm.describe(ans)
    alert.alert(lm_output)

