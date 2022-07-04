#--------------------------------------------------------------------------------------------------------------------------------------------#
import pandas as pd 
import matplotlib as plt 
import streamlit as stl 
from matplotlib import pyplot
#--------------------------------------------------------------------------------------------------------------------------------------------#
import missingno as msno
import plotly.express as px
import plotly.figure_factory as ff
from plotly.figure_factory import create_distplot
import matplotlib.pyplot as plt
from pylab import *
#---------------------------------------------------------------------------------------------------------------------------------------------#
from sklearn.preprocessing import StandardScaler
from sklearn import decomposition
from pca import pca
#---------------------------------------------------------------------------------------------------------------------------------------------#
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from bioinfokit.analys import get_data
from bioinfokit.visuz import cluster
#---------------------------------------------------------------------------------------------------------------------------------------------#
from mpl_toolkits.mplot3d import Axes3D
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
#----------------------------------------------------------------------------------------------------------------------------------------------#
from category_encoders import TargetEncoder
import category_encoders as ce
#----------------------------------------------------------------------------------------------------------------------------------------------#
import plotly.io as pio
pio.renderers.default='svg'
pio.renderers.default='browser'
#-----------------------------------------------------------------------------------------------------------------------------------------------#
import plotly.graph_objects as go
from imblearn.over_sampling import ADASYN
#-----------------------------------------------------------------------------------------------------------------------------------------------#
import xgboost as xgb
from xgboost import XGBClassifier
from xgboost import plot_importance
from xgboost import plot_tree
#-----------------------------------------------------------------------------------------------------------------------------------------------#
from sklearn.metrics import classification_report, confusion_matrix
#-----------------------------------------------------------------------------------------------------------------------------------------------#













