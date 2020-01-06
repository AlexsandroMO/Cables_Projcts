import numpy as np
import pandas as pd
import pandasql as ps
import sqlite3

def read_sql_queda(queda):
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT queda_tesao FROM cable_tabelacondutor
        WHERE secao = '{queda}';
	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()

	return read_db


def read_sql_corr(corr):
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT capacidade_conducao FROM cable_tabelacondutor
        WHERE secao = '{corr}';
	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()

	return read_db


def read_sql_dj(dj):
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT dj FROM cable_disjuntor
        WHERE dj = '{dj}';
	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()

	return read_db

def read_sql_filter(projeto):
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT project FROM cable_project
        WHERE id like '{projeto}';

	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db


def read_sql_filter_id(id_x):
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT id FROM cable_project
        WHERE project like '{id_x}';

	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db