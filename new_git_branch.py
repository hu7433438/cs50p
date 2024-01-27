#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/12/18 20:45
# @Author  : QingYang H.
# @File    : new_git_branch.py
import git


def new_git_branch(branch):
    repo = git.Repo(search_parent_directories=True)
    repo.git.checkout('main')
    new_head = repo.create_head(branch)
    new_head.checkout()


def create_py_file(p):
    with open(f'{p}.py', 'w') as file:
        file.write('')


if __name__ == '__main__':
    problem = input("What's problem name? ")
    new_git_branch(f'cs50/problems/2022/python/{problem}')
    create_py_file(problem)
