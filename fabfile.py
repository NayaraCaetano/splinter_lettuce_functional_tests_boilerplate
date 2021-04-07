# -​*- coding: utf-8 -*​-
import os
import os.path

from fabric.api import lcd, local, settings
from fabric.tasks import Task


class BaseInitializeTestService(Task):
    source_dir = 'dir/'

    def run(self, branch='develop'):
        self.prepare_source(branch)
        self.install_dependencies()
        self.init_service()

    def prepare_source(self, branch):
        self._clone_if_not_exist()
        with lcd(self.source_dir + self.project_dir):
            self.branch = branch if branch in self._get_directory_git_branches() else 'develop'
            local('git reset --hard')
            local('git checkout %s' % self.branch)
            local('git pull')

    def _clone_if_not_exist(self):
        if (os.path.isdir(self.source_dir + self.project_dir)):
            return True
        with settings(warn_only=True):
            local('mkdir %s' % self.source_dir)
        with lcd(self.source_dir):
            local('git clone %s' % self.git_url)

    def _get_directory_git_branches(self):
        out = local('git branch -r', capture=True)
        return out.replace('origin/', '').replace(' ', '').splitlines()

    def install_dependencies(self):
        with lcd(self.source_dir + self.project_dir):
            local('fab install_dependencies')

    def init_service(self):
        with settings(warn_only=True):
            local('sudo fuser -k %s/tcp' % self.http_port)
        with lcd(self.source_dir + self.project_dir):
            # init test server
            pass


class FunctionalTests(Task):

    name = 'functional_tests'

    pip_file = 'conf/requirements.txt'
    dependencies_apt_get_file = 'conf/apt-get-dependencies.txt'

    def run(self, feature='', scenarios=''):
        scenarios = self.parse_scenarios(scenarios)
        self.install_test_dependencies()
        self.init_tests(feature, scenarios)

    def parse_scenarios(self, scenarios):
        if not scenarios:
            return ''
        return '-s %s' % scenarios.replace('-', ',')

    def init_tests(self, feature, scenarios):
        command = 'lettuce functional_tests/features/%s %s --xunit-file=junit/functional_test_results.xml --with-xunit' % (feature, scenarios)
        local(command)

    def install_test_dependencies(self):
        print('----------Instalando dependências de teste...')
        with settings(warn_only=True):
            local('sudo apt-get install $(cat %s) -y' % self.dependencies_apt_get_file)
        local('pip install -r %s' % self.pip_file)
        print('----------Instalando dependências de teste...FIM!')


functional_tests = FunctionalTests()
