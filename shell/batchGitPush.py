# coding:UTF-8
# 当前文件夹下批量提交git
import os
from git import Repo
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


def add_commit_push(path, commit_msg):
    try:
        repo = Repo(path)
        index = repo.index
        index.add(['build.gradle', 'src/','.gitignore','gradlew','gradlew.bat','settings.gradle'])
        print "add success"
        index.commit(commit_msg)
        print "commit success"
        origin = repo.remotes['origin']
        origin.pull()
        print "pull success"
        origin.push()
        print "push success"
    except Exception as  e:
        print e.message
        print e


def batch_git_push(s_path, commit_msg):
    for s_child in os.listdir(s_path):
        s_child_path = os.path.join(s_path, s_child)
        add_commit_push(s_child_path, commit_msg)


# batch_git_push("C:/Users/user/Dropbox/tech/springboot/code", '增加eureka权限访问')
batch_git_push("C:/Users/user/Dropbox/tech/springboot/code", '服务器容错保护-hystrix')
# add_commit_push("C:/Users/user/Dropbox/tech/springboot/code/ribbon_peer1", '增加eureka权限访问')
