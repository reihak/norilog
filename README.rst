====================
乗りログアプリ
====================

目的
======

Webブラウザでコメントを投稿するwebアプリケーションの練習。

ツールのバージョン
==================

Python 3.6.5

pip 18.0

インストールと起動方法
======================

リポジトリーからコードを取得し、その下にvenv環境を用意します::

  $ git clone https://github.com/reihak/norilog.git

  $ cd norilog

  $ python3 -m venv venv

  $ source venv/bin/activate

  (venv) $ pip install .

  (venv) $ norilog

  * Running on http://127.0.0.1:8000/


  開発手順
  ==========

  開発様インストール
  =================

  1.チェックアウトする
  2.以下手順でインストールする

    (venv) $ pip install -e .
