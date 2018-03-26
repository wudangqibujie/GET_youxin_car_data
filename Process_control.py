import pickle
import hashlib





def save_progress(data):
    with open("prgress_control","wb") as f:
        pickle.dump(data,f)
def get_new_url(new_url):
    m = hashlib.md5()
    m.update(new_url.encode("utf-8"))
    md5_url = m.hexdigest()
    return md5_url
def load_progress():
    with open("prgress_control") as f:
        tmp = pickle.load(f)
        return tmp
