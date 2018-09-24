# coding:utf:8
import requests
from requests.adapters import HTTPAdapter
import json

requests.packages.urllib3.disable_warnings()

requests_retry = requests.Session()
requests_retry.mount('http://', HTTPAdapter(max_retries=3))
requests_retry.mount('https://', HTTPAdapter(max_retries=3))


class SaltStack(object):
    cookies = None
    host = None

    def __init__(self, host, username, password, port='8000',
                 secure=True, eproto='pam'):
        proto = 'https' if secure else 'http'
        self.host = '{}://{}:{}'.format(proto, host, port)

        self.login_url = self.host + "/login"
        self.logout_url = self.host + "/logout"
        self.minions_url = self.host + "/minions"
        self.jobs_url = self.host + "/jobs"
        self.run_url = self.host + "/run"
        self.events_url = self.host + "/events"
        self.ws_url = self.host + "/ws"
        self.hook_url = self.host + "/hook"
        self.stats_url = self.host + "/stats"

        if self.cookies is None:
            try:
                r = requests_retry.post(self.login_url, verify=False,
                                        data={'username': username,
                                              'password': password,
                                              'eauth': eproto},
                                        timeout=3)
                if r.status_code == 200:
                    self.cookies = r.cookies
                else:
                    raise Exception('Error from source %s' % r.text)
            except Exception as e:
                print(str(e))


    def cmd_run(self, tgt, arg,
                expr_form='compound', fun='cmd.run', timeout=600):
        try:
            r = requests_retry.post(self.host,
                                    verify=False, cookies=self.cookies,
                                    data={'tgt': tgt,
                                          'client': 'local',
                                          'expr_form': expr_form,
                                          'fun': fun,
                                          'timeout': timeout,
                                          'arg': arg})
            if r.status_code == 200:
                return r.json()
            else:
                raise Exception('Error from source %s' % r.text)
        except Exception as e:
            print(str(e))
    
    def cmd_script(self, tgt, arg,
                   expr_form='compound', fun='cmd.script'):
        try:
            r = requests_retry.post(self.host,
                                    verify=False, cookies=self.cookies,
                                    data={'tgt': tgt,
                                          'client': 'local',
                                          'expr_form': expr_form,
                                          'fun': fun,
                                          'arg': arg})
            if r.status_code == 200:
                return r.json()
            else:
                raise Exception('Error from source %s' % r.text)
        except Exception as e:
            print(str(e))


    def cp_file(self, tgt, from_path, to_path,
                expr_form='compound', timeout=60):
        try:
            if tgt and from_path and to_path:
                r = requests_retry.post(self.host, verify=False,
                                        cookies=self.cookies,
                                        data={'tgt': tgt,
                                              'client': 'local',
                                              'fun': 'cp.get_file',
                                              'arg': [from_path, to_path],
                                              'timeout': timeout,
                                              'makedirs': 'True',
                                              })
            else:
                data = {'return': 'Parameter is not enough.[API cp_file]'}
                return data
            if r.status_code == 200:
                return r.json()
            else:
                raise Exception('Error from source %s' % r.text)
        except Exception as e:
            print(str(e))

    def cp_dir(self, tgt, arg,
               expr_form='compound', timeout=500):
        try:
            if tgt and arg:
                r = requests_retry.post(self.host, verify=False,
                                        cookies=self.cookies,
                                        data={'tgt': tgt,
                                              'client': 'local',
                                              'fun': 'cp.get_dir',
                                              'arg': arg,
                                              'timeout': timeout,
                                              })
            else:
                data = {'return': 'Parameter is not enough.[API cp_dir]'}
                return data
            if r.status_code == 200:
                return r.json()
            else:
                raise Exception('Error from source %s' % r.text)
        except Exception as e:
            print(str(e))



def demo():
    sapi = SaltStack(host="192.168.1.111",
                     port='8899',
                     username="salt-api-client",
                     password="salt2018",
                     secure=True)
    # 为了语义明晰，使用列表
    attach_arg_list = [None]*9
    attach_arg_list[0] = "ZEP-BACKEND-JAVA"
    attach_arg_list[1] = "test"
    attach_arg_list[2] = "2018-0921-2023-34XZ"
    attach_arg_list[3] = "javademo-1.0.jar"
    attach_arg_list[4] = "18080"
    attach_arg_list[5] = "deploy"
    attach_arg_list[6] = "tot"
    attach_arg_list[7] = "http://192.168.1.111"
    attach_arg_list[8] = "javademo-1.0.tar.gz"

    # cmd_script后面附加参数为字符串，所以要进行转换
    attach_arg = ' '.join(attach_arg_list)
    
    result = sapi.cmd_script(tgt='192.168.1.112',
                             arg=["http://192.168.1.111/scripts/ZEP-BACKEND-JAVA.sh",
                                  attach_arg])
    
    print(result['return'][0]['192.168.1.112']['stdout'])

if __name__ == '__main__':
    demo()

