{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "ff35138a-6233-4ad0-b96f-a0fa74ee6372",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import hvplot.pandas\n",
    "import sqlalchemy\n",
    "from pathlib import Path\n",
    "import plotly.express as px\n",
    "\n",
    "code = {'Alabama': 'AL',\n",
    "        'Alaska': 'AK',\n",
    "        'Arizona': 'AZ',\n",
    "        'Arkansas': 'AR',\n",
    "        'California': 'CA',\n",
    "        'Colorado': 'CO',\n",
    "        'Connecticut': 'CT',\n",
    "        'Delaware': 'DE',\n",
    "        'District of Columbia': 'DC',\n",
    "        'Florida': 'FL',\n",
    "        'Georgia': 'GA',\n",
    "        'Hawaii': 'HI',\n",
    "        'Idaho': 'ID',\n",
    "        'Illinois': 'IL',\n",
    "        'Indiana': 'IN',\n",
    "        'Iowa': 'IA',\n",
    "        'Kansas': 'KS',\n",
    "        'Kentucky': 'KY',\n",
    "        'Louisiana': 'LA',\n",
    "        'Maine': 'ME',\n",
    "        'Maryland': 'MD',\n",
    "        'Massachusetts': 'MA',\n",
    "        'Michigan': 'MI',\n",
    "        'Minnesota': 'MN',\n",
    "        'Mississippi': 'MS',\n",
    "        'Missouri': 'MO',\n",
    "        'Montana': 'MT',\n",
    "        'Nebraska': 'NE',\n",
    "        'Nevada': 'NV',\n",
    "        'New Hampshire': 'NH',\n",
    "        'New Jersey': 'NJ',\n",
    "        'New Mexico': 'NM',\n",
    "        'New York': 'NY',\n",
    "        'North Carolina': 'NC',\n",
    "        'North Dakota': 'ND',\n",
    "        'Ohio': 'OH',\n",
    "        'Oklahoma': 'OK',\n",
    "        'Oregon': 'OR',\n",
    "        'Pennsylvania': 'PA',\n",
    "        'Rhode Island': 'RI',\n",
    "        'South Carolina': 'SC',\n",
    "        'South Dakota': 'SD',\n",
    "        'Tennessee': 'TN',\n",
    "        'Texas': 'TX',\n",
    "        'Utah': 'UT',\n",
    "        'Vermont': 'VT',\n",
    "        'Virginia': 'VA',\n",
    "        'Washington': 'WA',\n",
    "        'West Virginia': 'WV',\n",
    "        'Wisconsin': 'WI',\n",
    "        'Wyoming': 'WY'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "84920816-7957-4c19-8877-19a38bfbbbed",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Giselle\\anaconda3\\envs\\dev\\lib\\site-packages\\ipykernel_launcher.py:25: SADeprecationWarning:\n",
      "\n",
      "The Engine.table_names() method is deprecated and will be removed in a future release.  Please refer to Inspector.get_table_names(). (deprecated since: 1.4)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "#Student Population Data\n",
    "student_pop = pd.read_csv(\n",
    "    Path(\"../uncc_project1/other_datasets/pop_of_school_kids.csv\"))\n",
    "\n",
    "student_pop = student_pop.dropna()\n",
    "student_pop.tail()\n",
    "\n",
    "#School Finance Data\n",
    "\n",
    "state_school_fin = pd.read_csv(\n",
    "    Path(\"../uncc_project1/School_Data/states.csv\"))\n",
    "\n",
    "state_school_fin= state_school_fin.drop('ENROLL', axis=1)\n",
    "state_school_fin=state_school_fin.drop('OTHER_EXPENDITURE', axis=1)\n",
    "\n",
    "\n",
    "database_connection_string = \"sqlite://\"\n",
    "\n",
    "engine = sqlalchemy.create_engine(database_connection_string)\n",
    "\n",
    "engine\n",
    "\n",
    "school_db=state_school_fin.to_sql('school_finances', engine, index=False, if_exists='replace')\n",
    "\n",
    "engine.table_names()\n",
    "\n",
    "query_states_2016 = \"\"\"\n",
    "SELECT * \n",
    "FROM school_finances\n",
    "WHERE YEAR = 2016\n",
    "\"\"\"\n",
    "\n",
    "\n",
    "finance_2016=pd.read_sql_query(query_states_2016, con=engine)\n",
    "\n",
    "\n",
    "finance_2016[\"student_population\"] = student_pop[\"pop_2016\"]\n",
    "\n",
    "\n",
    "query_top10_rev = \"\"\"\n",
    "SELECT * \n",
    "FROM school_finances\n",
    "WHERE YEAR = 2016\n",
    "ORDER BY TOTAL_REVENUE DESC\n",
    "LIMIT 10\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "e1052a5e-70f5-41a6-a985-aeb9a19d3e71",
   "metadata": {},
   "outputs": [],
   "source": [
    "top10_rev = pd.read_sql_query(query_top10_rev, con=engine).sort_values('TOTAL_REVENUE', ascending=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "77a8f4c1-dc04-4eb0-a76e-b9b68010342c",
   "metadata": {},
   "outputs": [
    {
     "data": {},
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.holoviews_exec.v0+json": "",
      "text/html": [
       "<div id='1236'>\n",
       "\n",
       "\n",
       "\n",
       "\n",
       "\n",
       "  <div class=\"bk-root\" id=\"31de9915-48f3-4e76-9b96-b083fb04b208\" data-root-id=\"1236\"></div>\n",
       "</div>\n",
       "<script type=\"application/javascript\">(function(root) {\n",
       "  function embed_document(root) {\n",
       "    var docs_json = {\"d3aaaced-4a98-4d87-b76b-0cfbb8b2690f\":{\"defs\":[{\"extends\":null,\"module\":null,\"name\":\"ReactiveHTML1\",\"overrides\":[],\"properties\":[]},{\"extends\":null,\"module\":null,\"name\":\"FlexBox1\",\"overrides\":[],\"properties\":[{\"default\":\"flex-start\",\"kind\":null,\"name\":\"align_content\"},{\"default\":\"flex-start\",\"kind\":null,\"name\":\"align_items\"},{\"default\":\"row\",\"kind\":null,\"name\":\"flex_direction\"},{\"default\":\"wrap\",\"kind\":null,\"name\":\"flex_wrap\"},{\"default\":\"flex-start\",\"kind\":null,\"name\":\"justify_content\"}]},{\"extends\":null,\"module\":null,\"name\":\"TemplateActions1\",\"overrides\":[],\"properties\":[{\"default\":0,\"kind\":null,\"name\":\"open_modal\"},{\"default\":0,\"kind\":null,\"name\":\"close_modal\"}]},{\"extends\":null,\"module\":null,\"name\":\"MaterialTemplateActions1\",\"overrides\":[],\"properties\":[{\"default\":0,\"kind\":null,\"name\":\"open_modal\"},{\"default\":0,\"kind\":null,\"name\":\"close_modal\"}]}],\"roots\":{\"references\":[{\"attributes\":{\"below\":[{\"id\":\"1250\"}],\"center\":[{\"id\":\"1252\"},{\"id\":\"1256\"}],\"height\":300,\"left\":[{\"id\":\"1253\"}],\"margin\":[5,5,5,5],\"min_border_bottom\":10,\"min_border_left\":10,\"min_border_right\":10,\"min_border_top\":10,\"renderers\":[{\"id\":\"1276\"}],\"sizing_mode\":\"fixed\",\"title\":{\"id\":\"1242\"},\"toolbar\":{\"id\":\"1263\"},\"width\":700,\"x_range\":{\"id\":\"1238\"},\"x_scale\":{\"id\":\"1246\"},\"y_range\":{\"id\":\"1239\"},\"y_scale\":{\"id\":\"1248\"}},\"id\":\"1241\",\"subtype\":\"Figure\",\"type\":\"Plot\"},{\"attributes\":{},\"id\":\"1280\",\"type\":\"AllLabels\"},{\"attributes\":{},\"id\":\"1282\",\"type\":\"CategoricalTickFormatter\"},{\"attributes\":{\"fill_color\":{\"value\":\"#30a2da\"},\"top\":{\"field\":\"TOTAL_REVENUE\"},\"width\":{\"value\":0.8},\"x\":{\"field\":\"STATE\"}},\"id\":\"1273\",\"type\":\"VBar\"},{\"attributes\":{\"data\":{\"STATE\":[\"California\",\"New York\",\"Texas\",\"Illinois\",\"Pennsylvania\",\"New Jersey\",\"Florida\",\"Ohio\",\"Michigan\",\"Georgia\"],\"TOTAL_REVENUE\":[89217262,66912661,58284155,32908958,31077289,30012666,28125598,23766529,19416061,19403453]},\"selected\":{\"id\":\"1271\"},\"selection_policy\":{\"id\":\"1295\"}},\"id\":\"1270\",\"type\":\"ColumnDataSource\"},{\"attributes\":{\"overlay\":{\"id\":\"1262\"}},\"id\":\"1260\",\"type\":\"BoxZoomTool\"},{\"attributes\":{},\"id\":\"1248\",\"type\":\"LinearScale\"},{\"attributes\":{\"data_source\":{\"id\":\"1270\"},\"glyph\":{\"id\":\"1273\"},\"hover_glyph\":null,\"muted_glyph\":{\"id\":\"1275\"},\"nonselection_glyph\":{\"id\":\"1274\"},\"selection_glyph\":{\"id\":\"1278\"},\"view\":{\"id\":\"1277\"}},\"id\":\"1276\",\"type\":\"GlyphRenderer\"},{\"attributes\":{},\"id\":\"1285\",\"type\":\"AllLabels\"},{\"attributes\":{\"axis_label\":\"Total Revenue\",\"formatter\":{\"id\":\"1279\"},\"major_label_policy\":{\"id\":\"1285\"},\"ticker\":{\"id\":\"1254\"}},\"id\":\"1253\",\"type\":\"LinearAxis\"},{\"attributes\":{},\"id\":\"1261\",\"type\":\"ResetTool\"},{\"attributes\":{\"text\":\"Top 10 States for School Revenue\",\"text_color\":\"black\",\"text_font_size\":\"12pt\"},\"id\":\"1242\",\"type\":\"Title\"},{\"attributes\":{\"format\":\"%.0f\"},\"id\":\"1279\",\"type\":\"PrintfTickFormatter\"},{\"attributes\":{\"margin\":[5,5,5,5],\"name\":\"HSpacer01931\",\"sizing_mode\":\"stretch_width\"},\"id\":\"1237\",\"type\":\"Spacer\"},{\"attributes\":{\"bottom_units\":\"screen\",\"fill_alpha\":0.5,\"fill_color\":\"lightgrey\",\"left_units\":\"screen\",\"level\":\"overlay\",\"line_alpha\":1.0,\"line_color\":\"black\",\"line_dash\":[4,4],\"line_width\":2,\"right_units\":\"screen\",\"syncable\":false,\"top_units\":\"screen\"},\"id\":\"1262\",\"type\":\"BoxAnnotation\"},{\"attributes\":{\"factors\":[\"California\",\"New York\",\"Texas\",\"Illinois\",\"Pennsylvania\",\"New Jersey\",\"Florida\",\"Ohio\",\"Michigan\",\"Georgia\"],\"tags\":[[[\"STATE\",\"STATE\",null]]]},\"id\":\"1238\",\"type\":\"FactorRange\"},{\"attributes\":{},\"id\":\"1271\",\"type\":\"Selection\"},{\"attributes\":{},\"id\":\"1246\",\"type\":\"CategoricalScale\"},{\"attributes\":{},\"id\":\"1254\",\"type\":\"BasicTicker\"},{\"attributes\":{},\"id\":\"1251\",\"type\":\"CategoricalTicker\"},{\"attributes\":{\"callback\":null,\"renderers\":[{\"id\":\"1276\"}],\"tags\":[\"hv_created\"],\"tooltips\":[[\"STATE\",\"@{STATE}\"],[\"TOTAL_REVENUE\",\"@{TOTAL_REVENUE}\"]]},\"id\":\"1240\",\"type\":\"HoverTool\"},{\"attributes\":{},\"id\":\"1258\",\"type\":\"PanTool\"},{\"attributes\":{\"source\":{\"id\":\"1270\"}},\"id\":\"1277\",\"type\":\"CDSView\"},{\"attributes\":{},\"id\":\"1259\",\"type\":\"WheelZoomTool\"},{\"attributes\":{},\"id\":\"1295\",\"type\":\"UnionRenderers\"},{\"attributes\":{\"axis\":{\"id\":\"1250\"},\"grid_line_color\":null,\"ticker\":null},\"id\":\"1252\",\"type\":\"Grid\"},{\"attributes\":{\"fill_alpha\":{\"value\":0.1},\"fill_color\":{\"value\":\"#30a2da\"},\"line_alpha\":{\"value\":0.1},\"top\":{\"field\":\"TOTAL_REVENUE\"},\"width\":{\"value\":0.8},\"x\":{\"field\":\"STATE\"}},\"id\":\"1274\",\"type\":\"VBar\"},{\"attributes\":{\"fill_alpha\":{\"value\":0.2},\"fill_color\":{\"value\":\"#30a2da\"},\"line_alpha\":{\"value\":0.2},\"top\":{\"field\":\"TOTAL_REVENUE\"},\"width\":{\"value\":0.8},\"x\":{\"field\":\"STATE\"}},\"id\":\"1275\",\"type\":\"VBar\"},{\"attributes\":{},\"id\":\"1257\",\"type\":\"SaveTool\"},{\"attributes\":{\"children\":[{\"id\":\"1237\"},{\"id\":\"1241\"},{\"id\":\"1306\"}],\"margin\":[0,0,0,0],\"name\":\"Row01927\",\"tags\":[\"embedded\"]},\"id\":\"1236\",\"type\":\"Row\"},{\"attributes\":{\"end\":90000000,\"reset_end\":90000000,\"reset_start\":10000000,\"start\":10000000,\"tags\":[[[\"TOTAL_REVENUE\",\"TOTAL_REVENUE\",null]]]},\"id\":\"1239\",\"type\":\"Range1d\"},{\"attributes\":{\"margin\":[5,5,5,5],\"name\":\"HSpacer01932\",\"sizing_mode\":\"stretch_width\"},\"id\":\"1306\",\"type\":\"Spacer\"},{\"attributes\":{\"formatter\":{\"id\":\"1282\"},\"major_label_orientation\":0.7853981633974483,\"major_label_policy\":{\"id\":\"1280\"},\"ticker\":{\"id\":\"1251\"}},\"id\":\"1250\",\"type\":\"CategoricalAxis\"},{\"attributes\":{\"bottom\":{\"value\":0},\"fill_alpha\":{\"value\":1.0},\"fill_color\":{\"value\":\"#30a2da\"},\"hatch_alpha\":{\"value\":1.0},\"hatch_color\":{\"value\":\"black\"},\"hatch_scale\":{\"value\":12.0},\"hatch_weight\":{\"value\":1.0},\"line_alpha\":{\"value\":1.0},\"line_cap\":{\"value\":\"butt\"},\"line_color\":{\"value\":\"black\"},\"line_dash\":{\"value\":[]},\"line_dash_offset\":{\"value\":0},\"line_join\":{\"value\":\"bevel\"},\"line_width\":{\"value\":1},\"top\":{\"field\":\"TOTAL_REVENUE\"},\"width\":{\"value\":0.8},\"x\":{\"field\":\"STATE\"}},\"id\":\"1278\",\"type\":\"VBar\"},{\"attributes\":{\"axis\":{\"id\":\"1253\"},\"dimension\":1,\"grid_line_color\":null,\"ticker\":null},\"id\":\"1256\",\"type\":\"Grid\"},{\"attributes\":{\"active_multi\":null,\"tools\":[{\"id\":\"1240\"},{\"id\":\"1257\"},{\"id\":\"1258\"},{\"id\":\"1259\"},{\"id\":\"1260\"},{\"id\":\"1261\"}]},\"id\":\"1263\",\"type\":\"Toolbar\"}],\"root_ids\":[\"1236\"]},\"title\":\"Bokeh Application\",\"version\":\"2.3.2\"}};\n",
       "    var render_items = [{\"docid\":\"d3aaaced-4a98-4d87-b76b-0cfbb8b2690f\",\"root_ids\":[\"1236\"],\"roots\":{\"1236\":\"31de9915-48f3-4e76-9b96-b083fb04b208\"}}];\n",
       "    root.Bokeh.embed.embed_items_notebook(docs_json, render_items);\n",
       "  }\n",
       "  if (root.Bokeh !== undefined && root.Bokeh.Panel !== undefined) {\n",
       "    embed_document(root);\n",
       "  } else {\n",
       "    var attempts = 0;\n",
       "    var timer = setInterval(function(root) {\n",
       "      if (root.Bokeh !== undefined && root.Bokeh.Panel !== undefined) {\n",
       "        clearInterval(timer);\n",
       "        embed_document(root);\n",
       "      } else if (document.readyState == \"complete\") {\n",
       "        attempts++;\n",
       "        if (attempts > 200) {\n",
       "          clearInterval(timer);\n",
       "          console.log(\"Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing\");\n",
       "        }\n",
       "      }\n",
       "    }, 25, root)\n",
       "  }\n",
       "})(window);</script>"
      ],
      "text/plain": [
       ":Bars   [STATE]   (TOTAL_REVENUE)"
      ]
     },
     "execution_count": 45,
     "metadata": {
      "application/vnd.holoviews_exec.v0+json": {
       "id": "1236"
      }
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "top10_graph = top10_rev[['STATE','TOTAL_REVENUE']].hvplot.bar(\n",
    "    x='STATE',\n",
    "    y='TOTAL_REVENUE',\n",
    "    rot=45,\n",
    "    yformatter='%.0f',\n",
    "    ylim=[10000000,90000000],\n",
    "    title='Top 10 States for School Revenue',\n",
    "    ylabel='Total Revenue',\n",
    "    xlabel=''\n",
    ")\n",
    "\n",
    "top10_graph"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "f7255a0c-1f5e-4323-8a68-7799f9e81ff8",
   "metadata": {},
   "outputs": [],
   "source": [
    "query_bottom10_rev = \"\"\"\n",
    "SELECT * \n",
    "FROM school_finances\n",
    "WHERE YEAR = 2016\n",
    "ORDER BY TOTAL_REVENUE ASC\n",
    "LIMIT 10\n",
    "\"\"\"\n",
    "\n",
    "bottom10_rev = pd.read_sql_query(query_bottom10_rev, con=engine)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "e7c6c8a0-9e67-4da3-b59e-329d6f9054e0",
   "metadata": {},
   "outputs": [
    {
     "data": {},
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.holoviews_exec.v0+json": "",
      "text/html": [
       "<div id='1353'>\n",
       "\n",
       "\n",
       "\n",
       "\n",
       "\n",
       "  <div class=\"bk-root\" id=\"8837950b-536d-4e16-a9bc-7a20d8bdd71a\" data-root-id=\"1353\"></div>\n",
       "</div>\n",
       "<script type=\"application/javascript\">(function(root) {\n",
       "  function embed_document(root) {\n",
       "    var docs_json = {\"4acbc6e8-dff8-474f-84ff-22fdfde3d4db\":{\"defs\":[{\"extends\":null,\"module\":null,\"name\":\"ReactiveHTML1\",\"overrides\":[],\"properties\":[]},{\"extends\":null,\"module\":null,\"name\":\"FlexBox1\",\"overrides\":[],\"properties\":[{\"default\":\"flex-start\",\"kind\":null,\"name\":\"align_content\"},{\"default\":\"flex-start\",\"kind\":null,\"name\":\"align_items\"},{\"default\":\"row\",\"kind\":null,\"name\":\"flex_direction\"},{\"default\":\"wrap\",\"kind\":null,\"name\":\"flex_wrap\"},{\"default\":\"flex-start\",\"kind\":null,\"name\":\"justify_content\"}]},{\"extends\":null,\"module\":null,\"name\":\"TemplateActions1\",\"overrides\":[],\"properties\":[{\"default\":0,\"kind\":null,\"name\":\"open_modal\"},{\"default\":0,\"kind\":null,\"name\":\"close_modal\"}]},{\"extends\":null,\"module\":null,\"name\":\"MaterialTemplateActions1\",\"overrides\":[],\"properties\":[{\"default\":0,\"kind\":null,\"name\":\"open_modal\"},{\"default\":0,\"kind\":null,\"name\":\"close_modal\"}]}],\"roots\":{\"references\":[{\"attributes\":{\"axis_label\":\"Total Revenue\",\"formatter\":{\"id\":\"1396\"},\"major_label_policy\":{\"id\":\"1402\"},\"ticker\":{\"id\":\"1371\"}},\"id\":\"1370\",\"type\":\"LinearAxis\"},{\"attributes\":{\"fill_alpha\":{\"value\":0.1},\"fill_color\":{\"value\":\"#30a2da\"},\"line_alpha\":{\"value\":0.1},\"top\":{\"field\":\"TOTAL_REVENUE\"},\"width\":{\"value\":0.8},\"x\":{\"field\":\"STATE\"}},\"id\":\"1391\",\"type\":\"VBar\"},{\"attributes\":{\"margin\":[5,5,5,5],\"name\":\"HSpacer02082\",\"sizing_mode\":\"stretch_width\"},\"id\":\"1423\",\"type\":\"Spacer\"},{\"attributes\":{\"active_multi\":null,\"tools\":[{\"id\":\"1357\"},{\"id\":\"1374\"},{\"id\":\"1375\"},{\"id\":\"1376\"},{\"id\":\"1377\"},{\"id\":\"1378\"}]},\"id\":\"1380\",\"type\":\"Toolbar\"},{\"attributes\":{\"axis\":{\"id\":\"1370\"},\"dimension\":1,\"grid_line_color\":null,\"ticker\":null},\"id\":\"1373\",\"type\":\"Grid\"},{\"attributes\":{\"fill_color\":{\"value\":\"#30a2da\"},\"top\":{\"field\":\"TOTAL_REVENUE\"},\"width\":{\"value\":0.8},\"x\":{\"field\":\"STATE\"}},\"id\":\"1390\",\"type\":\"VBar\"},{\"attributes\":{},\"id\":\"1397\",\"type\":\"AllLabels\"},{\"attributes\":{\"fill_alpha\":{\"value\":0.2},\"fill_color\":{\"value\":\"#30a2da\"},\"line_alpha\":{\"value\":0.2},\"top\":{\"field\":\"TOTAL_REVENUE\"},\"width\":{\"value\":0.8},\"x\":{\"field\":\"STATE\"}},\"id\":\"1392\",\"type\":\"VBar\"},{\"attributes\":{\"bottom_units\":\"screen\",\"fill_alpha\":0.5,\"fill_color\":\"lightgrey\",\"left_units\":\"screen\",\"level\":\"overlay\",\"line_alpha\":1.0,\"line_color\":\"black\",\"line_dash\":[4,4],\"line_width\":2,\"right_units\":\"screen\",\"syncable\":false,\"top_units\":\"screen\"},\"id\":\"1379\",\"type\":\"BoxAnnotation\"},{\"attributes\":{\"callback\":null,\"renderers\":[{\"id\":\"1393\"}],\"tags\":[\"hv_created\"],\"tooltips\":[[\"STATE\",\"@{STATE}\"],[\"TOTAL_REVENUE\",\"@{TOTAL_REVENUE}\"]]},\"id\":\"1357\",\"type\":\"HoverTool\"},{\"attributes\":{\"data_source\":{\"id\":\"1387\"},\"glyph\":{\"id\":\"1390\"},\"hover_glyph\":null,\"muted_glyph\":{\"id\":\"1392\"},\"nonselection_glyph\":{\"id\":\"1391\"},\"selection_glyph\":{\"id\":\"1395\"},\"view\":{\"id\":\"1394\"}},\"id\":\"1393\",\"type\":\"GlyphRenderer\"},{\"attributes\":{\"children\":[{\"id\":\"1354\"},{\"id\":\"1358\"},{\"id\":\"1423\"}],\"margin\":[0,0,0,0],\"name\":\"Row02077\",\"tags\":[\"embedded\"]},\"id\":\"1353\",\"type\":\"Row\"},{\"attributes\":{\"factors\":[\"District of Columbia\",\"South Dakota\",\"North Dakota\",\"Montana\",\"Delaware\",\"Wyoming\",\"Vermont\",\"Idaho\",\"Rhode Island\",\"Alaska\"],\"tags\":[[[\"STATE\",\"STATE\",null]]]},\"id\":\"1355\",\"type\":\"FactorRange\"},{\"attributes\":{\"end\":2600000,\"reset_end\":2600000,\"reset_start\":500000,\"start\":500000,\"tags\":[[[\"TOTAL_REVENUE\",\"TOTAL_REVENUE\",null]]]},\"id\":\"1356\",\"type\":\"Range1d\"},{\"attributes\":{\"source\":{\"id\":\"1387\"}},\"id\":\"1394\",\"type\":\"CDSView\"},{\"attributes\":{\"bottom\":{\"value\":0},\"fill_alpha\":{\"value\":1.0},\"fill_color\":{\"value\":\"#30a2da\"},\"hatch_alpha\":{\"value\":1.0},\"hatch_color\":{\"value\":\"black\"},\"hatch_scale\":{\"value\":12.0},\"hatch_weight\":{\"value\":1.0},\"line_alpha\":{\"value\":1.0},\"line_cap\":{\"value\":\"butt\"},\"line_color\":{\"value\":\"black\"},\"line_dash\":{\"value\":[]},\"line_dash_offset\":{\"value\":0},\"line_join\":{\"value\":\"bevel\"},\"line_width\":{\"value\":1},\"top\":{\"field\":\"TOTAL_REVENUE\"},\"width\":{\"value\":0.8},\"x\":{\"field\":\"STATE\"}},\"id\":\"1395\",\"type\":\"VBar\"},{\"attributes\":{},\"id\":\"1388\",\"type\":\"Selection\"},{\"attributes\":{},\"id\":\"1402\",\"type\":\"AllLabels\"},{\"attributes\":{},\"id\":\"1374\",\"type\":\"SaveTool\"},{\"attributes\":{\"below\":[{\"id\":\"1367\"}],\"center\":[{\"id\":\"1369\"},{\"id\":\"1373\"}],\"height\":300,\"left\":[{\"id\":\"1370\"}],\"margin\":[5,5,5,5],\"min_border_bottom\":10,\"min_border_left\":10,\"min_border_right\":10,\"min_border_top\":10,\"renderers\":[{\"id\":\"1393\"}],\"sizing_mode\":\"fixed\",\"title\":{\"id\":\"1359\"},\"toolbar\":{\"id\":\"1380\"},\"width\":700,\"x_range\":{\"id\":\"1355\"},\"x_scale\":{\"id\":\"1363\"},\"y_range\":{\"id\":\"1356\"},\"y_scale\":{\"id\":\"1365\"}},\"id\":\"1358\",\"subtype\":\"Figure\",\"type\":\"Plot\"},{\"attributes\":{},\"id\":\"1375\",\"type\":\"PanTool\"},{\"attributes\":{},\"id\":\"1378\",\"type\":\"ResetTool\"},{\"attributes\":{\"text\":\"Bottom 10 States for School Revenue\",\"text_color\":\"black\",\"text_font_size\":\"12pt\"},\"id\":\"1359\",\"type\":\"Title\"},{\"attributes\":{},\"id\":\"1399\",\"type\":\"CategoricalTickFormatter\"},{\"attributes\":{},\"id\":\"1376\",\"type\":\"WheelZoomTool\"},{\"attributes\":{\"axis\":{\"id\":\"1367\"},\"grid_line_color\":null,\"ticker\":null},\"id\":\"1369\",\"type\":\"Grid\"},{\"attributes\":{\"format\":\"%.0f\"},\"id\":\"1396\",\"type\":\"PrintfTickFormatter\"},{\"attributes\":{\"overlay\":{\"id\":\"1379\"}},\"id\":\"1377\",\"type\":\"BoxZoomTool\"},{\"attributes\":{},\"id\":\"1412\",\"type\":\"UnionRenderers\"},{\"attributes\":{\"margin\":[5,5,5,5],\"name\":\"HSpacer02081\",\"sizing_mode\":\"stretch_width\"},\"id\":\"1354\",\"type\":\"Spacer\"},{\"attributes\":{},\"id\":\"1371\",\"type\":\"BasicTicker\"},{\"attributes\":{\"formatter\":{\"id\":\"1399\"},\"major_label_orientation\":0.7853981633974483,\"major_label_policy\":{\"id\":\"1397\"},\"ticker\":{\"id\":\"1368\"}},\"id\":\"1367\",\"type\":\"CategoricalAxis\"},{\"attributes\":{\"data\":{\"STATE\":[\"District of Columbia\",\"South Dakota\",\"North Dakota\",\"Montana\",\"Delaware\",\"Wyoming\",\"Vermont\",\"Idaho\",\"Rhode Island\",\"Alaska\"],\"TOTAL_REVENUE\":[1329719,1455737,1788749,1800909,2043577,2044669,2112365,2266490,2401541,2494691]},\"selected\":{\"id\":\"1388\"},\"selection_policy\":{\"id\":\"1412\"}},\"id\":\"1387\",\"type\":\"ColumnDataSource\"},{\"attributes\":{},\"id\":\"1363\",\"type\":\"CategoricalScale\"},{\"attributes\":{},\"id\":\"1365\",\"type\":\"LinearScale\"},{\"attributes\":{},\"id\":\"1368\",\"type\":\"CategoricalTicker\"}],\"root_ids\":[\"1353\"]},\"title\":\"Bokeh Application\",\"version\":\"2.3.2\"}};\n",
       "    var render_items = [{\"docid\":\"4acbc6e8-dff8-474f-84ff-22fdfde3d4db\",\"root_ids\":[\"1353\"],\"roots\":{\"1353\":\"8837950b-536d-4e16-a9bc-7a20d8bdd71a\"}}];\n",
       "    root.Bokeh.embed.embed_items_notebook(docs_json, render_items);\n",
       "  }\n",
       "  if (root.Bokeh !== undefined && root.Bokeh.Panel !== undefined) {\n",
       "    embed_document(root);\n",
       "  } else {\n",
       "    var attempts = 0;\n",
       "    var timer = setInterval(function(root) {\n",
       "      if (root.Bokeh !== undefined && root.Bokeh.Panel !== undefined) {\n",
       "        clearInterval(timer);\n",
       "        embed_document(root);\n",
       "      } else if (document.readyState == \"complete\") {\n",
       "        attempts++;\n",
       "        if (attempts > 200) {\n",
       "          clearInterval(timer);\n",
       "          console.log(\"Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing\");\n",
       "        }\n",
       "      }\n",
       "    }, 25, root)\n",
       "  }\n",
       "})(window);</script>"
      ],
      "text/plain": [
       ":Bars   [STATE]   (TOTAL_REVENUE)"
      ]
     },
     "execution_count": 47,
     "metadata": {
      "application/vnd.holoviews_exec.v0+json": {
       "id": "1353"
      }
     },
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bottom10_graph = bottom10_rev[['STATE','TOTAL_REVENUE']].hvplot.bar(\n",
    "    x='STATE',\n",
    "    y='TOTAL_REVENUE',\n",
    "    rot=45,\n",
    "    yformatter='%.0f',\n",
    "    ylim=[500000,2600000],\n",
    "    title='Bottom 10 States for School Revenue',\n",
    "    ylabel='Total Revenue',\n",
    "    xlabel=''\n",
    ") \n",
    "bottom10_graph"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "eadc62b8-2704-4f41-990b-ecd0cb1f8309",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Comparing School Finance Data w/ Drug Abuse and Mental Health data 2015 to 2016\n",
    "alcoholism_2016 = pd.read_csv(\n",
    "    Path(\"../uncc_project1/other_datasets/drug_abuse_data/alcoholism_2016.csv\"))\n",
    "alcoholism_2016.loc[:, \"12-17 Estimate\"] = alcoholism_2016.loc[:, \"12-17 Estimate\"].str.replace(\"%\", \"\")\n",
    "alcoholism_2016=alcoholism_2016.drop([0,1,2,3,4])\n",
    "\n",
    "alcoholism_2016=alcoholism_2016.reset_index(drop=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "35c3536b-6959-44f4-961b-e18b947d82d9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "coloraxis": "coloraxis",
         "geo": "geo",
         "hovertemplate": "<b>%{hovertext}</b><br><br>Code=%{location}<br>color=%{z}<extra></extra>",
         "hovertext": [
          "Alabama",
          "Alaska",
          "Arizona",
          "Arkansas",
          "California",
          "Colorado",
          "Connecticut",
          "Delaware",
          "District of Columbia",
          "Florida",
          "Georgia",
          "Hawaii",
          "Idaho",
          "Illinois",
          "Indiana",
          "Iowa",
          "Kansas",
          "Kentucky",
          "Louisiana",
          "Maine",
          "Maryland",
          "Massachusetts",
          "Michigan",
          "Minnesota",
          "Mississippi",
          "Missouri",
          "Montana",
          "Nebraska",
          "Nevada",
          "New Hampshire",
          "New Jersey",
          "New Mexico",
          "New York",
          "North Carolina",
          "North Dakota",
          "Ohio",
          "Oklahoma",
          "Oregon",
          "Pennsylvania",
          "Rhode Island",
          "South Carolina",
          "South Dakota",
          "Tennessee",
          "Texas",
          "Utah",
          "Vermont",
          "Virginia",
          "Washington",
          "West Virginia",
          "Wisconsin",
          "Wyoming"
         ],
         "locationmode": "USA-states",
         "locations": [
          "AL",
          "AK",
          "AZ",
          "AR",
          "CA",
          "CO",
          "CT",
          "DE",
          "DC",
          "FL",
          "GA",
          "HI",
          "ID",
          "IL",
          "IN",
          "IA",
          "KS",
          "KY",
          "LA",
          "ME",
          "MD",
          "MA",
          "MI",
          "MN",
          "MS",
          "MO",
          "MT",
          "NE",
          "NV",
          "NH",
          "NJ",
          "NM",
          "NY",
          "NC",
          "ND",
          "OH",
          "OK",
          "OR",
          "PA",
          "RI",
          "SC",
          "SD",
          "TN",
          "TX",
          "UT",
          "VT",
          "VA",
          "WA",
          "WV",
          "WI",
          "WY"
         ],
         "name": "",
         "type": "choropleth",
         "z": [
          1.67,
          2.59,
          2.28,
          2.14,
          2.33,
          2.6,
          2.82,
          2.08,
          1.88,
          2.2,
          1.73,
          2.35,
          2.56,
          2.25,
          2.07,
          2.46,
          2.36,
          2.08,
          2.6,
          2.42,
          1.99,
          2.56,
          2.36,
          2.16,
          1.68,
          2.21,
          2.91,
          2.43,
          2.59,
          2.28,
          2.19,
          2.76,
          2.21,
          1.62,
          2.82,
          2.16,
          2.09,
          2.79,
          2.12,
          2.32,
          2.11,
          2.87,
          1.85,
          2.38,
          1.87,
          2.6,
          2.08,
          2.3,
          2.14,
          2.63,
          2.86
         ]
        }
       ],
       "layout": {
        "coloraxis": {
         "cmax": 3,
         "cmin": 1,
         "colorbar": {
          "title": {
           "text": "% of Children"
          }
         },
         "colorscale": [
          [
           0,
           "rgb(94,79,162)"
          ],
          [
           0.1,
           "rgb(50,136,189)"
          ],
          [
           0.2,
           "rgb(102,194,165)"
          ],
          [
           0.3,
           "rgb(171,221,164)"
          ],
          [
           0.4,
           "rgb(230,245,152)"
          ],
          [
           0.5,
           "rgb(255,255,191)"
          ],
          [
           0.6,
           "rgb(254,224,139)"
          ],
          [
           0.7,
           "rgb(253,174,97)"
          ],
          [
           0.8,
           "rgb(244,109,67)"
          ],
          [
           0.9,
           "rgb(213,62,79)"
          ],
          [
           1,
           "rgb(158,1,66)"
          ]
         ]
        },
        "geo": {
         "center": {
          "lat": 36.416661444627216,
          "lon": -96.5817414338416
         },
         "domain": {
          "x": [
           0,
           1
          ],
          "y": [
           0,
           1
          ]
         },
         "projection": {
          "scale": 0.9999999999999998
         },
         "scope": "usa"
        },
        "height": 500,
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "l": 5,
         "r": 10
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Alcoholism Among Children Age 12-17"
        },
        "width": 700
       }
      },
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABEAAAAH0CAYAAAA9nFiLAAAgAElEQVR4nOzdd3BUd773+ae2trZqa2urnq3a2tqqfWZumrnzDGOP89jGHoPUJ3ZSzjlLiKyAEDkjCZElgUBgECCRRDLJGAMyOAAGjAPJBmMbnMHXxgIB0mf/kFuWmu5WS2rpJ53+vKq+9TwXSx2ORN973vzO7/w3EBEREREREREZ3H8T/QKIiIiIiIiIiPoaAwgRERERERERGR4DCBEREREREREZHgMIERERERERERkeAwgRERERERERGR4DCBEREREREREZHgMIERERERERERkeAwgRERERERERGR4DCBEREREREREZHgMIERERERERERkeAwgRERERERERGR4DCBEREREREREZHgMIERERERERERkeAwgRERERERERGR4DCBEREREREREZHgMIERERERERERkeAwgRERERERERGR4DCBEREREREREZHgMIERERERERERkeAwgRERERERERGR4DCBEREREREREZHgMIERERERERERkeAwgRERERERERGR4DCBEREREREREZHgMIERERERERERkeAwgRERERERERGR4DCBEREREREREZHgMIERERERERERkeAwgRERERERERGR4DCBEREREREREZHgMIERERERERERkeAwgRERERERERGR4DCBEREREREREZHgMIERERERERERkeAwgRERERERERGR4DCBEREREREREZHgNIB6WVdRgyLAkfXbrWJ4+fN6MSQ4YlDfjHJPEOHj2JIcOSsG7LgR59f2zuLARGjOvy6z66dA1DhiWhtLKuR89DREREREQ0WPhNAHGc6Hk62TNKABkyLMmrk18RAiPGYciwJMTmzhL9UoRZt+VA++9ixzl49GT713QngDh+Bzp+v9ECSMdj1vF9DgSllXUej3XHzx7H9Pb33/GYro6F43fH0wy0Y0hERERE1B/8JoA44oanOMAA0recT8z66jgPZO5OQB2/e3kzKgEwgDiLzZ3Vfuwcx2ggcBw/d8fa8d+dg0dv/446jkd3QwZXjBERERGRP/ObABIYMQ6xubPaTzRdnTgYJYAMVB1P1AfDSbevOU5a3fno0rUeBRB3z2WUANLxNXZ1DPuL8yoeTwHE1bF1fH93f769WckxGH7WRERERER9yS8CSMeTScdJgKt/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",
      "text/html": [
       "<div>                            <div id=\"7fd9d80d-2d47-43ea-b070-ac44e2c181a8\" class=\"plotly-graph-div\" style=\"height:500px; width:700px;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"7fd9d80d-2d47-43ea-b070-ac44e2c181a8\")) {                    Plotly.newPlot(                        \"7fd9d80d-2d47-43ea-b070-ac44e2c181a8\",                        [{\"coloraxis\":\"coloraxis\",\"geo\":\"geo\",\"hovertemplate\":\"<b>%{hovertext}</b><br><br>Code=%{location}<br>color=%{z}<extra></extra>\",\"hovertext\":[\"Alabama\",\"Alaska\",\"Arizona\",\"Arkansas\",\"California\",\"Colorado\",\"Connecticut\",\"Delaware\",\"District of Columbia\",\"Florida\",\"Georgia\",\"Hawaii\",\"Idaho\",\"Illinois\",\"Indiana\",\"Iowa\",\"Kansas\",\"Kentucky\",\"Louisiana\",\"Maine\",\"Maryland\",\"Massachusetts\",\"Michigan\",\"Minnesota\",\"Mississippi\",\"Missouri\",\"Montana\",\"Nebraska\",\"Nevada\",\"New Hampshire\",\"New Jersey\",\"New Mexico\",\"New York\",\"North Carolina\",\"North Dakota\",\"Ohio\",\"Oklahoma\",\"Oregon\",\"Pennsylvania\",\"Rhode Island\",\"South Carolina\",\"South Dakota\",\"Tennessee\",\"Texas\",\"Utah\",\"Vermont\",\"Virginia\",\"Washington\",\"West Virginia\",\"Wisconsin\",\"Wyoming\"],\"locationmode\":\"USA-states\",\"locations\":[\"AL\",\"AK\",\"AZ\",\"AR\",\"CA\",\"CO\",\"CT\",\"DE\",\"DC\",\"FL\",\"GA\",\"HI\",\"ID\",\"IL\",\"IN\",\"IA\",\"KS\",\"KY\",\"LA\",\"ME\",\"MD\",\"MA\",\"MI\",\"MN\",\"MS\",\"MO\",\"MT\",\"NE\",\"NV\",\"NH\",\"NJ\",\"NM\",\"NY\",\"NC\",\"ND\",\"OH\",\"OK\",\"OR\",\"PA\",\"RI\",\"SC\",\"SD\",\"TN\",\"TX\",\"UT\",\"VT\",\"VA\",\"WA\",\"WV\",\"WI\",\"WY\"],\"name\":\"\",\"type\":\"choropleth\",\"z\":[1.67,2.59,2.28,2.14,2.33,2.6,2.82,2.08,1.88,2.2,1.73,2.35,2.56,2.25,2.07,2.46,2.36,2.08,2.6,2.42,1.99,2.56,2.36,2.16,1.68,2.21,2.91,2.43,2.59,2.28,2.19,2.76,2.21,1.62,2.82,2.16,2.09,2.79,2.12,2.32,2.11,2.87,1.85,2.38,1.87,2.6,2.08,2.3,2.14,2.63,2.86]}],                        {\"coloraxis\":{\"cmax\":3,\"cmin\":1,\"colorbar\":{\"title\":{\"text\":\"% of Children\"}},\"colorscale\":[[0.0,\"rgb(94,79,162)\"],[0.1,\"rgb(50,136,189)\"],[0.2,\"rgb(102,194,165)\"],[0.3,\"rgb(171,221,164)\"],[0.4,\"rgb(230,245,152)\"],[0.5,\"rgb(255,255,191)\"],[0.6,\"rgb(254,224,139)\"],[0.7,\"rgb(253,174,97)\"],[0.8,\"rgb(244,109,67)\"],[0.9,\"rgb(213,62,79)\"],[1.0,\"rgb(158,1,66)\"]]},\"geo\":{\"center\":{},\"domain\":{\"x\":[0.0,1.0],\"y\":[0.0,1.0]},\"scope\":\"usa\"},\"height\":500,\"legend\":{\"tracegroupgap\":0},\"margin\":{\"l\":5,\"r\":10},\"template\":{\"data\":{\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"title\":{\"text\":\"Alcoholism Among Children Age 12-17\"},\"width\":700},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('7fd9d80d-2d47-43ea-b070-ac44e2c181a8');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "alcoholism_2016['Code'] = alcoholism_2016['State'].map(code)\n",
    "fig = px.choropleth(alcoholism_2016,\n",
    "                    locations='Code',\n",
    "                    color= alcoholism_2016['12-17 Estimate'].astype(float),\n",
    "                    range_color=[1,3],\n",
    "                    color_continuous_scale='spectral_r',\n",
    "                    hover_name='State',\n",
    "                    locationmode='USA-states',\n",
    "                    title=\"Alcoholism Among Children Age 12-17\",\n",
    "                    scope='usa',\n",
    "                    width=700,\n",
    "                    height=500,\n",
    "                   )\n",
    "fig.update_layout(coloraxis_colorbar=dict(\n",
    "    title=\"% of Children\"))\n",
    "fig= fig.update_layout(margin_l=5)\n",
    "fig=fig.update_layout(margin_r=10)\n",
    "fig"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "285ac4b9-6ac6-4f4f-a450-37fb731e1931",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "coloraxis": "coloraxis",
         "geo": "geo",
         "hovertemplate": "<b>%{hovertext}</b><br><br>Code=%{location}<br>color=%{z}<extra></extra>",
         "hovertext": [
          "Alabama",
          "Alaska",
          "Arizona",
          "Arkansas",
          "California",
          "Colorado",
          "Connecticut",
          "Delaware",
          "District of Columbia",
          "Florida",
          "Georgia",
          "Hawaii",
          "Idaho",
          "Illinois",
          "Indiana",
          "Iowa",
          "Kansas",
          "Kentucky",
          "Louisiana",
          "Maine",
          "Maryland",
          "Massachusetts",
          "Michigan",
          "Minnesota",
          "Mississippi",
          "Missouri",
          "Montana",
          "Nebraska",
          "Nevada",
          "New Hampshire",
          "New Jersey",
          "New Mexico",
          "New York",
          "North Carolina",
          "North Dakota",
          "Ohio",
          "Oklahoma",
          "Oregon",
          "Pennsylvania",
          "Rhode Island",
          "South Carolina",
          "South Dakota",
          "Tennessee",
          "Texas",
          "Utah",
          "Vermont",
          "Virginia",
          "Washington",
          "West Virginia",
          "Wisconsin",
          "Wyoming"
         ],
         "locationmode": "USA-states",
         "locations": [
          "AL",
          "AK",
          "AZ",
          "AR",
          "CA",
          "CO",
          "CT",
          "DE",
          "DC",
          "FL",
          "GA",
          "HI",
          "ID",
          "IL",
          "IN",
          "IA",
          "KS",
          "KY",
          "LA",
          "ME",
          "MD",
          "MA",
          "MI",
          "MN",
          "MS",
          "MO",
          "MT",
          "NE",
          "NV",
          "NH",
          "NJ",
          "NM",
          "NY",
          "NC",
          "ND",
          "OH",
          "OK",
          "OR",
          "PA",
          "RI",
          "SC",
          "SD",
          "TN",
          "TX",
          "UT",
          "VT",
          "VA",
          "WA",
          "WV",
          "WI",
          "WY"
         ],
         "name": "",
         "type": "choropleth",
         "z": [
          1.5427420176132511,
          3.364284539096615,
          1.230782257931443,
          1.8074292114632369,
          2.2703629200745636,
          1.8305748263369321,
          3.183019969701911,
          2.145041765596233,
          1.9430791307194126,
          1.361579978185169,
          1.8813426323638063,
          2.1211976344647483,
          1.3490803118523165,
          2.563856380231239,
          1.9192263438974364,
          2.2100819293301637,
          2.0873880699418206,
          1.7461070085455443,
          1.7919024053184731,
          2.1390186072805344,
          2.3916869939210774,
          2.5623415728749754,
          1.9546150404013916,
          2.2056153337978843,
          1.5928770371958338,
          1.788362542799617,
          1.7338839808367736,
          2.3059362980662117,
          1.525178157450836,
          2.3598783534267405,
          3.3427573416068044,
          1.8054144177321534,
          3.373245425076045,
          1.3240579681035818,
          2.367485586620572,
          2.0448628588862654,
          1.5565941813324315,
          1.81548579793044,
          2.4303654038430182,
          2.2708190316254493,
          1.847176572062465,
          1.68968779235371,
          1.4415323538771294,
          2.0886738303884105,
          1.6269384864473884,
          3.388708502712744,
          1.9323199094882808,
          2.0552808197409838,
          1.854703257125389,
          2.0262660973646427,
          3.4956984835273803
         ]
        }
       ],
       "layout": {
        "coloraxis": {
         "colorbar": {
          "title": {
           "text": "USD"
          }
         },
         "colorscale": [
          [
           0,
           "rgb(94,79,162)"
          ],
          [
           0.1,
           "rgb(50,136,189)"
          ],
          [
           0.2,
           "rgb(102,194,165)"
          ],
          [
           0.3,
           "rgb(171,221,164)"
          ],
          [
           0.4,
           "rgb(230,245,152)"
          ],
          [
           0.5,
           "rgb(255,255,191)"
          ],
          [
           0.6,
           "rgb(254,224,139)"
          ],
          [
           0.7,
           "rgb(253,174,97)"
          ],
          [
           0.8,
           "rgb(244,109,67)"
          ],
          [
           0.9,
           "rgb(213,62,79)"
          ],
          [
           1,
           "rgb(158,1,66)"
          ]
         ]
        },
        "geo": {
         "center": {
          "lat": 37.43929419243062,
          "lon": -84.67101143721572
         },
         "domain": {
          "x": [
           0,
           1
          ],
          "y": [
           0,
           1
          ]
         },
         "projection": {
          "scale": 1.161508731925722
         },
         "scope": "usa"
        },
        "height": 500,
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "l": 5,
         "r": 10
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "School Revenue Per Capita"
        },
        "width": 700
       }
      },
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABEAAAAH0CAYAAAA9nFiLAAAgAElEQVR4nOzdd3Cb937n+83uTia35O7NnZ2d3M1u7j1OcpM49eTM5iQn56xzJAAPAJIASRDsvfdOir33JpJiJ0WJRY0qpHqxRHWr+Ei2umRLlm1JlOWiYh9ZpGTpc/9QIJMQQIIkwB8IfV4z35lzIJQHD+BnBm8+5d+BiIiIiIiIiMjB/TvRC0BEREREREREZGsMIERERERERETk8BhAiIiIiIiIiMjhMYAQERERERERkcNjACEiIiIiIiIih8cAQkREREREREQOjwGEiIiIiIiIiBweAwgREREREREROTwGECIiIiIiIiJyeAwgREREREREROTwGECIiIiIiIiIyOExgBARERERERGRw2MAISIiIiIiIiKHxwBCRERERERERA6PAYSIiIiIiIiIHB4DCBERERERERE5PAYQIiIiIiIiInJ4DCBERERERERE5PAYQIiIiIiIiIjI4TGAEBEREREREZHDYwAhIiIiIiIiIofHAEJEREREREREDo8BhIiIiIiIiIgcHgMIERERERERETk8BhAiIiIiIiIicngMIERERERERETk8BhAiIiIiIiIiMjhMYAQERERERERkcNjACEiIiIiIiIih8cAQkREREREREQOjwGEiIiIiIiIiBweAwgREREREREROTwGECIiIiIiIiJyeAwgREREREREROTwGECIiIiIiIiIyOExgBARERERERGRw2MAmaW04ja8/U6QkNfee+g03n4nCH1De4S8PhEREREREdFi9UYEkL6hPXj7naDXZi4hYbEEkJq2dSbfs6hlX0wM69l4luhThCyPuc/y4rWbNn1dw3d976HTr25bok+Bb1ypTV+XiIiIiIjIFhw+gPjGlb72Iw748cddTdu6WT3fYgsgxu97iT7F5O30I8N6Nv5uGNadrcODwcVrN83Gjrl+f2eDAYSIiIiIiByJQwcQw54f5oLBxWs337gAYvhRnVbcZqvFXPTMBRDDuluoALBEnzLtXid7D522aQAxhQGEiIiIiIgWqzcigMx2bwfDX/pNHW4wOYBYcmiJqcNvTJn8137DGC+3rQOI4b0ZxviH7nQ//k39WDc+dMPUj3nDshivJ+PlM/feDe/HVAgw/hwtjQXmAoi59znToVWTv4eT1/F0yzNTvDO3zMZjLuLUtK177fMxvq/h3w3ffVP/XUz+Ppv6N8YSIiIiIiKyFw4dQAw/Ci09d4O5OGD4gW7436ZChqm/jBvuO/nwBVO3mfqxa+o2awSQmQ7vML5t8roz/kFs/JyTX8tw6NHk+xpum8xU8DD1PmcTQEztqTGbPV8sDSCG+5la9smPnRx3LA0apr4nMy2z8ffc1LJMDm2mlnHy8pn6vKfbA8TU8jKCEBERERGRvXDoAALM7gSSvnGlM8YSc4fAGP9YnGnPhMk/Cs39qDR+LWsEEFM/SM2FDcN7MLzedIFo8nqbbs8b43ViLkoYr5PZBBBzn6NhuWaKCuYCiPHt5j43w/o0ft3Z7IlkKhbNhW9cqckQZOp7abzeZhtATDFeF0RERERERKI4fAAxMHWIifGPUkv2ELA0gEz3o3fyc0z3g9T4OaxxFRhTyzNd+DFeNuP3b2r5pztPyhJ9ypR1bIsAYu45Te2pYoq5ADJ5zx9LPjdLvgvmzDWAmDpMZfJnO91yG3+H5xJAjA+jmi44EhERERERLaQ3JoAYM/wQNPw4nO6H4WSWBhBze1VMfo6L125OGzWMD0uYzx4gkwOQMXPndrDk8BRTf+E3/Hg3N5N/QFs7gJgLXZNnpvVn7nwaptbDdGNY9/MJIJaGA8PnYBwnjOOWrQLI5PUx3XMSERERERGJ8sYGEOD1v7I74h4gk1/f3DlRjA+TmMnkH8HGe3QY3p+l512x1R4g87k6ynTnADF+XUs+i7kEkNmeBNVcmJhNADH+bs8mgFj63wUREREREZEoDh1AatrWTfvDy/jHnLlDQS5eu/naSVBNvdbkH3r2eg4Qw+2To8Nsf6Qafpybe43Z/OC3RQCx5Fwu07EkgJhaRnPmejUic3vsGEy+jLO59TibAGL8fkx9L8zFMnPrnAGEiIiIiIjshcMHEFN7PAA/7v1hag+JyT8kjf/SP5u/dBvuO/k1prsKzExX5bBGAJm8DJNfz9RVYAz3NfV6pg5nmczcIRyGy69Ofh5LAoip28xd0cTUVWAmP8dcT4Jq7n6mln/yupxrAJn8/oyX2fgzNHXOEMNtpgKIqb12jF/H1HfaXNAw9X2bfB4aBhAiIiIiIhLNoQMIYP5cDdP95d74vpac4NPcD8PJl0Cd7i/6ps5dYe4StvMNIMCPP44nrwdzJ7A0xXDf6ZbFkivwzCaAGO5vGEPMmG6Phtl87gaWBhBTy2SYye9prgHEwNLPxfjcK3sPnTa7B4ipdWPM3Hfa+HWM7z/5vxvuAUJERERERPbC4QMIEf3I0pP9EhERERERORoGEKI3CAMIERERERG9qRhAiN4gDCBERERERPSmYgAhIiIiIiIiIofHAEJEREREREREDo8BhIiIiIiIiIgcHgMIERERERERETk8BhAiIiIiIiIicngMIERERERERETk8BhAiIiIiIiIiMjhMYAQERERERERkcNjACEiIiIiIiIih8cAQkREREREREQOjwGEiIiIiIiIiBweAwgREREREREROTwGECIiIiIiIiJyeAwgREREREREROTwGECIiIiIiIiIyOExgBARERERERGRw2MAISIiIiIiIiKHxwBCRERERERERA6PAYSIiIiIiIiIHB4DCBERERERERE5PAYQIiIiIiIiInJ4DCBERERERERE5PAYQIiIiIiIiIjI4TGAEBEREREREZHDYwAhIiIiIiIiIofHAEJEREREREREDo8BhIiIiIiIiIgcHgMIERERERERETk8BhAiIiIiIiIicngMIERERERERETk8BhAiIiIiIiIiMjhMYAQERERERERkcNjACEiIiIiIiIih8cAQkREREREREQOjwGEiIiIiIiIiBweAwgREREREREROTwGECIiIiIiIiJyeAwgREREREREROTwGECIiIiIiIiIyOExgBARERERERGRw2MAISIiIiIiIiKHxwBCRERERERERA6PAYSIiIiIiIiIHB4DCBERERERERE5PAYQIiIiIiIiInJ4DCBERERERERE5PAYQIiIiIiIiIjI4TGAEBEREREREZHDYwAhIiIiIiIiIofHAEJEREREREREDo8BhIiIiIiIiIgcHgMIERERERERETk8BhAiIiIiIiIicngMIERERERERETk8BhAiIiIiIiIiMjhMYAQkV168uSJ6EUgIiIiIiIHwgBCRHbpyZMn0Go1yC/MwbZt23Dr1i3Ri0RERERERIsYAwgR2aUnT55ApVaidzgP2aVR0Hu5IzDYH83NzTh69CgeP34sehGJiIiIiGgRYQAhIpsaGxub0+PGx8ehVqtw7uueV7PrN7VoWpWOpPQISJICScnxGBgYwKVLl6y81ERERERE5GgYQIjIZm7cuAFXN1ccOHBg1o8dHx+HSq2cEkAm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",
      "text/html": [
       "<div>                            <div id=\"85ef1d05-82c0-437f-bb74-8df06565c77b\" class=\"plotly-graph-div\" style=\"height:500px; width:700px;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"85ef1d05-82c0-437f-bb74-8df06565c77b\")) {                    Plotly.newPlot(                        \"85ef1d05-82c0-437f-bb74-8df06565c77b\",                        [{\"coloraxis\":\"coloraxis\",\"geo\":\"geo\",\"hovertemplate\":\"<b>%{hovertext}</b><br><br>Code=%{location}<br>color=%{z}<extra></extra>\",\"hovertext\":[\"Alabama\",\"Alaska\",\"Arizona\",\"Arkansas\",\"California\",\"Colorado\",\"Connecticut\",\"Delaware\",\"District of Columbia\",\"Florida\",\"Georgia\",\"Hawaii\",\"Idaho\",\"Illinois\",\"Indiana\",\"Iowa\",\"Kansas\",\"Kentucky\",\"Louisiana\",\"Maine\",\"Maryland\",\"Massachusetts\",\"Michigan\",\"Minnesota\",\"Mississippi\",\"Missouri\",\"Montana\",\"Nebraska\",\"Nevada\",\"New Hampshire\",\"New Jersey\",\"New Mexico\",\"New York\",\"North Carolina\",\"North Dakota\",\"Ohio\",\"Oklahoma\",\"Oregon\",\"Pennsylvania\",\"Rhode Island\",\"South Carolina\",\"South Dakota\",\"Tennessee\",\"Texas\",\"Utah\",\"Vermont\",\"Virginia\",\"Washington\",\"West Virginia\",\"Wisconsin\",\"Wyoming\"],\"locationmode\":\"USA-states\",\"locations\":[\"AL\",\"AK\",\"AZ\",\"AR\",\"CA\",\"CO\",\"CT\",\"DE\",\"DC\",\"FL\",\"GA\",\"HI\",\"ID\",\"IL\",\"IN\",\"IA\",\"KS\",\"KY\",\"LA\",\"ME\",\"MD\",\"MA\",\"MI\",\"MN\",\"MS\",\"MO\",\"MT\",\"NE\",\"NV\",\"NH\",\"NJ\",\"NM\",\"NY\",\"NC\",\"ND\",\"OH\",\"OK\",\"OR\",\"PA\",\"RI\",\"SC\",\"SD\",\"TN\",\"TX\",\"UT\",\"VT\",\"VA\",\"WA\",\"WV\",\"WI\",\"WY\"],\"name\":\"\",\"type\":\"choropleth\",\"z\":[1.5427420176132511,3.364284539096615,1.230782257931443,1.8074292114632369,2.2703629200745636,1.8305748263369321,3.183019969701911,2.145041765596233,1.9430791307194126,1.361579978185169,1.8813426323638063,2.1211976344647483,1.3490803118523165,2.563856380231239,1.9192263438974364,2.2100819293301637,2.0873880699418206,1.7461070085455443,1.7919024053184731,2.1390186072805344,2.3916869939210774,2.5623415728749754,1.9546150404013916,2.2056153337978843,1.5928770371958338,1.788362542799617,1.7338839808367736,2.3059362980662117,1.525178157450836,2.3598783534267405,3.3427573416068044,1.8054144177321534,3.373245425076045,1.3240579681035818,2.367485586620572,2.0448628588862654,1.5565941813324315,1.81548579793044,2.4303654038430182,2.2708190316254493,1.847176572062465,1.68968779235371,1.4415323538771294,2.0886738303884105,1.6269384864473884,3.388708502712744,1.9323199094882808,2.0552808197409838,1.854703257125389,2.0262660973646427,3.4956984835273803]}],                        {\"coloraxis\":{\"colorbar\":{\"title\":{\"text\":\"USD\"}},\"colorscale\":[[0.0,\"rgb(94,79,162)\"],[0.1,\"rgb(50,136,189)\"],[0.2,\"rgb(102,194,165)\"],[0.3,\"rgb(171,221,164)\"],[0.4,\"rgb(230,245,152)\"],[0.5,\"rgb(255,255,191)\"],[0.6,\"rgb(254,224,139)\"],[0.7,\"rgb(253,174,97)\"],[0.8,\"rgb(244,109,67)\"],[0.9,\"rgb(213,62,79)\"],[1.0,\"rgb(158,1,66)\"]]},\"geo\":{\"center\":{},\"domain\":{\"x\":[0.0,1.0],\"y\":[0.0,1.0]},\"scope\":\"usa\"},\"height\":500,\"legend\":{\"tracegroupgap\":0},\"margin\":{\"l\":5,\"r\":10},\"template\":{\"data\":{\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"title\":{\"text\":\"School Revenue Per Capita\"},\"width\":700},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('85ef1d05-82c0-437f-bb74-8df06565c77b');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Add per capita row\n",
    "\n",
    "finance_2016= pd.DataFrame(finance_2016)\n",
    "\n",
    "finance_2016[\"rev_per_capita\"]=finance_2016[\"TOTAL_REVENUE\"]/finance_2016[\"student_population\"]\n",
    "\n",
    "finance_2016\n",
    "\n",
    "\n",
    "#Funding per capita heat map\n",
    "\n",
    "finance_2016['Code'] = finance_2016['STATE'].map(code)\n",
    "fig = px.choropleth(finance_2016,\n",
    "                    locations='Code',\n",
    "                    color= finance_2016['rev_per_capita'].astype(float),\n",
    "                    color_continuous_scale='spectral_r',\n",
    "                    hover_name='STATE',\n",
    "                    locationmode='USA-states',\n",
    "                    title=\"School Revenue Per Capita\",\n",
    "                    scope='usa',\n",
    "                    width=700,\n",
    "                    height=500,\n",
    "                   )\n",
    "fig.update_layout(coloraxis_colorbar=dict(\n",
    "    title=\"USD\"))\n",
    "fig= fig.update_layout(margin_l=5)\n",
    "fig_finance_heat=fig.update_layout(margin_r=10)\n",
    "fig_finance_heat"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "06a8b6cb-bd1e-41fc-bbd7-6ae5f74d30f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Major Depressive Episodes\n",
    "depressive_2016 = pd.read_csv(\n",
    "    Path(\"../uncc_project1/other_datasets/drug_abuse_data/major_depressive_episode_2016.csv\"))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "1d8867eb-b732-469a-8dd1-4a5dde54a942",
   "metadata": {},
   "outputs": [],
   "source": [
    "depressive_2016.loc[:,\"12-17 Estimate\"] = depressive_2016.loc[:,\"12-17 Estimate\"].str.replace(\"%\", \"\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "b4572c80-8640-4caf-b342-ae80b4377ad2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "coloraxis": "coloraxis",
         "geo": "geo",
         "hovertemplate": "<b>%{hovertext}</b><br><br>Code=%{location}<br>color=%{z}<extra></extra>",
         "hovertext": [
          "Total U.S.",
          "Northeast",
          "Midwest",
          "South",
          "West",
          "Alabama",
          "Alaska",
          "Arizona",
          "Arkansas",
          "California",
          "Colorado",
          "Connecticut",
          "Delaware",
          "District of Columbia",
          "Florida",
          "Georgia",
          "Hawaii",
          "Idaho",
          "Illinois",
          "Indiana",
          "Iowa",
          "Kansas",
          "Kentucky",
          "Louisiana",
          "Maine",
          "Maryland",
          "Massachusetts",
          "Michigan",
          "Minnesota",
          "Mississippi",
          "Missouri",
          "Montana",
          "Nebraska",
          "Nevada",
          "New Hampshire",
          "New Jersey",
          "New Mexico",
          "New York",
          "North Carolina",
          "North Dakota",
          "Ohio",
          "Oklahoma",
          "Oregon",
          "Pennsylvania",
          "Rhode Island",
          "South Carolina",
          "South Dakota",
          "Tennessee",
          "Texas",
          "Utah",
          "Vermont",
          "Virginia",
          "Washington",
          "West Virginia",
          "Wisconsin",
          "Wyoming"
         ],
         "locationmode": "USA-states",
         "locations": [
          null,
          null,
          null,
          null,
          null,
          "AL",
          "AK",
          "AZ",
          "AR",
          "CA",
          "CO",
          "CT",
          "DE",
          "DC",
          "FL",
          "GA",
          "HI",
          "ID",
          "IL",
          "IN",
          "IA",
          "KS",
          "KY",
          "LA",
          "ME",
          "MD",
          "MA",
          "MI",
          "MN",
          "MS",
          "MO",
          "MT",
          "NE",
          "NV",
          "NH",
          "NJ",
          "NM",
          "NY",
          "NC",
          "ND",
          "OH",
          "OK",
          "OR",
          "PA",
          "RI",
          "SC",
          "SD",
          "TN",
          "TX",
          "UT",
          "VT",
          "VA",
          "WA",
          "WV",
          "WI",
          "WY"
         ],
         "name": "",
         "type": "choropleth",
         "z": [
          12.63,
          12.13,
          13.53,
          11.9,
          13.32,
          11.18,
          15.22,
          11.68,
          13.05,
          12.93,
          14.59,
          12.52,
          11.94,
          9.91,
          12.84,
          10.14,
          10.99,
          15.93,
          12.46,
          14.7,
          14.09,
          12.53,
          11.72,
          10.15,
          14.25,
          12.69,
          13.72,
          13.27,
          13.39,
          10.78,
          14.28,
          13.56,
          12.97,
          15.66,
          13.4,
          10.39,
          12.61,
          11.91,
          11.7,
          11.25,
          13.98,
          13.53,
          15.66,
          12.33,
          13.72,
          10.83,
          11.79,
          12.13,
          11.95,
          13.81,
          12.45,
          12.56,
          13.23,
          13.9,
          14.45,
          15
         ]
        }
       ],
       "layout": {
        "coloraxis": {
         "cmax": 16,
         "cmin": 9,
         "colorbar": {
          "title": {
           "text": "% of Children"
          }
         },
         "colorscale": [
          [
           0,
           "rgb(94,79,162)"
          ],
          [
           0.1,
           "rgb(50,136,189)"
          ],
          [
           0.2,
           "rgb(102,194,165)"
          ],
          [
           0.3,
           "rgb(171,221,164)"
          ],
          [
           0.4,
           "rgb(230,245,152)"
          ],
          [
           0.5,
           "rgb(255,255,191)"
          ],
          [
           0.6,
           "rgb(254,224,139)"
          ],
          [
           0.7,
           "rgb(253,174,97)"
          ],
          [
           0.8,
           "rgb(244,109,67)"
          ],
          [
           0.9,
           "rgb(213,62,79)"
          ],
          [
           1,
           "rgb(158,1,66)"
          ]
         ]
        },
        "geo": {
         "center": {
          "lat": 29.03946498076941,
          "lon": -78.56275909664299
         },
         "domain": {
          "x": [
           0,
           1
          ],
          "y": [
           0,
           1
          ]
         },
         "projection": {
          "scale": 30.909476069641723
         },
         "scope": "usa"
        },
        "height": 500,
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "l": 5,
         "r": 10
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Major Depressive Episode Among Children Ages 12-17 in 2016"
        },
        "width": 700
       }
      },
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABEAAAAH0CAYAAAA9nFiLAAAgAElEQVR4nOzdeXBUd373+6du3brUc3NTeZInN5XUfZJJMjOZGU8ySWaSTCZx4tjq7tN7q7Xv+y6hBUloA7QggUBICJAEEhKbBMKA2MVidjC2AYNtGcxujG3wCnhsDBIgfe4fPK1pml5Oq7v1k1qfV9W3akZIrdNHreM+b53lv4GIiIiIiIiIyM/9N9ELQERERERERETkawwgREREREREROT3GECIiIiIiIiIyO8xgBARERERERGR32MAISIiIiIiIiK/xwBCRERERERERH6PAYSIiIiIiIiI/B4DCBERERERERH5PQYQIiIiIiIiIvJ7DCBERERERERE5PcYQIiIiIiIiIjI7zGAEBEREREREZHfYwAhIiIiIiIiIr/HAEJEREREREREfo8BhIiIiIiIiIj8HgMIEREREREREfk9BhAiIiIiIiIi8nsMIERERERERETk9xhAiIiIiIiIiMjvMYAQERERERERkd9jACEiIiIiIiIiv8cAQkRERERERER+jwGEiIiIiIiIiPweAwgRERERERER+T0GECIiIiIiIiLyewwgREREREREROT3GECIiIiIiIiIyO8xgBARERERERGR32MAISIiIiIiIiK/xwBCRERERERERH6PAYSIiIiIiIiI/B4DCBERERERERH5PQYQIiIiIiIiIvJ7DCBERERERERE5PcYQIiIiIiIiIjI7zGAEBEREREREZHfYwAholFrN+3DCy/FY//R06IXZcp74aV4FFa3jelrF7b14oWX4nH+8g2Xn/tKaAGisueO6fsQEREREU0mfh9AXngp3umOhGVH4YWX4sf8PSw7jQvbesf8GO6yLLPtvBJaMG7LMJGI+BnYfm9v/kz2Hz3t0Q7wWPk6gBRWt3n8+zbZnb98w+7rxPa1K/fnb++1728BxHqdifgd95TlZ+SML7blL7wUj7Wb9j33cUevQeux93XWfLmNsv7vsqvlsfdcXG2/Frb1ylq/ludoPURERDS5TZkA4uiNizfe2IgKIPZ2WqKy5wrZcRZtIgQQVzsM7vDXAOLODpY/svx+2r5OLT9v650yBpDfsd4hnoyR19V/Y+w9r1dCCzz675IlNrr7eyb3teOrbZTl+1svt6Ptu2UZrD/uahtmCSauXkeW31UiIiLy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IzeAAO5tRzwJII4ukmvh6HRCe69z23Uh5znI2TbJ5SqAWJbRm+REh7E+H8B3AcSdi43aW345/0119Rq0Fyvl3vGJiIiIJjYGENh/c2q9c2PZMXHnCBDrj1uPbQzwJIDYG7k7pLZj/f0tOx7OPkfustu7doejnRHrsV2X9pbH+jGcvcG2/NxcrRt7yynnyAdX18mwdxcYV8/X3mvN3uvJ3g6m7WvXVfixfixXRz/ZjqudFDl/XbY9rNzTAGL9cXfXsbPHtF1fr4QW2D2tyhVH10SxXT5vBxDg+Wtq7D962q0jQCzkbkfGGkDk7Ji7ujW35TXt6JQXOc9BzrbJ1XNwtV2Rcx0id15f9rYvlnH0uWPhqwDi6rovju4Q5Wp752w77ey0QWfrj4iIiCYfvw8g48Eb10mYSHiYr++4ewtQmtg8uZ4EjQ9PrkdERERERP6FAcQL3L3F4UTHAOI7DCCTl+3v+FgvHkm+Ye+UrLHefYSIiIiI/BMDyBjZHhrtT1eFZwDxHQaQyUvOaSskjqPTtPzlyDwiIiIi8hwDCBERERERERH5PQYQIiIiIiIiIvJ7DCBERERERERE5PcYQIiIiIiIiIjI7zGAEBEREREREZHfYwAhIiIiIiIiIr/HAEJEREREREREfo8BhIiIiIiIiIj8HgMIEREREREREfk9BhAiIiIiIiIi8nsMIERERERERETk9xhAiIiIiIiIiMjvMYAQERERERERkd9jACEiIiIiIiIiv8cAQkRERERERER+jwGEiIiIiIiIiPweAwgRERERERER+T0GECIiIiIiIiLyewwgREREREREROT3GECIiIiIiIiIyO8xgBARERERERGR32MAISIiIiIiIiK/xwBCRERERERERH6PAYSIiIiIiIiI/B4DCBERERERERH5PQYQIiIiIiIiIvJ7DCBERERERERE5PcYQIiIiIiIiIjI7zGAEBEREREREZHfYwAhIiIiIiIiIr/HAEJEREREREREfo8BhIiIiIiIiIj8HgMIEREREREREfk9BhAiIiIiIiIi8nsMIERERERERETk9xhAiIiIiIiIiMjvMYAQERERERERkd9jACEiIiIiIiIiv8cAQkRERERERER+jwGEiIiIiIiIiPweAwgRERERERER+T0GECIiIiIiIiLyewwgREREREREROT3GECIiIiIiIiIyO8x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AAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPYIIAAAAAAAwPb+P+WzYeCVX6ZbAAAAAElFTkSuQmCC",
      "text/html": [
       "<div>                            <div id=\"cfc02413-ceeb-4a96-8a3e-0b425ab1fd8c\" class=\"plotly-graph-div\" style=\"height:500px; width:700px;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"cfc02413-ceeb-4a96-8a3e-0b425ab1fd8c\")) {                    Plotly.newPlot(                        \"cfc02413-ceeb-4a96-8a3e-0b425ab1fd8c\",                        [{\"coloraxis\":\"coloraxis\",\"geo\":\"geo\",\"hovertemplate\":\"<b>%{hovertext}</b><br><br>Code=%{location}<br>color=%{z}<extra></extra>\",\"hovertext\":[\"Total U.S.\",\"Northeast\",\"Midwest\",\"South\",\"West\",\"Alabama\",\"Alaska\",\"Arizona\",\"Arkansas\",\"California\",\"Colorado\",\"Connecticut\",\"Delaware\",\"District of Columbia\",\"Florida\",\"Georgia\",\"Hawaii\",\"Idaho\",\"Illinois\",\"Indiana\",\"Iowa\",\"Kansas\",\"Kentucky\",\"Louisiana\",\"Maine\",\"Maryland\",\"Massachusetts\",\"Michigan\",\"Minnesota\",\"Mississippi\",\"Missouri\",\"Montana\",\"Nebraska\",\"Nevada\",\"New Hampshire\",\"New Jersey\",\"New Mexico\",\"New York\",\"North Carolina\",\"North Dakota\",\"Ohio\",\"Oklahoma\",\"Oregon\",\"Pennsylvania\",\"Rhode Island\",\"South Carolina\",\"South Dakota\",\"Tennessee\",\"Texas\",\"Utah\",\"Vermont\",\"Virginia\",\"Washington\",\"West Virginia\",\"Wisconsin\",\"Wyoming\"],\"locationmode\":\"USA-states\",\"locations\":[null,null,null,null,null,\"AL\",\"AK\",\"AZ\",\"AR\",\"CA\",\"CO\",\"CT\",\"DE\",\"DC\",\"FL\",\"GA\",\"HI\",\"ID\",\"IL\",\"IN\",\"IA\",\"KS\",\"KY\",\"LA\",\"ME\",\"MD\",\"MA\",\"MI\",\"MN\",\"MS\",\"MO\",\"MT\",\"NE\",\"NV\",\"NH\",\"NJ\",\"NM\",\"NY\",\"NC\",\"ND\",\"OH\",\"OK\",\"OR\",\"PA\",\"RI\",\"SC\",\"SD\",\"TN\",\"TX\",\"UT\",\"VT\",\"VA\",\"WA\",\"WV\",\"WI\",\"WY\"],\"name\":\"\",\"type\":\"choropleth\",\"z\":[12.63,12.13,13.53,11.9,13.32,11.18,15.22,11.68,13.05,12.93,14.59,12.52,11.94,9.91,12.84,10.14,10.99,15.93,12.46,14.7,14.09,12.53,11.72,10.15,14.25,12.69,13.72,13.27,13.39,10.78,14.28,13.56,12.97,15.66,13.4,10.39,12.61,11.91,11.7,11.25,13.98,13.53,15.66,12.33,13.72,10.83,11.79,12.13,11.95,13.81,12.45,12.56,13.23,13.9,14.45,15.0]}],                        {\"coloraxis\":{\"cmax\":16,\"cmin\":9,\"colorbar\":{\"title\":{\"text\":\"% of Children\"}},\"colorscale\":[[0.0,\"rgb(94,79,162)\"],[0.1,\"rgb(50,136,189)\"],[0.2,\"rgb(102,194,165)\"],[0.3,\"rgb(171,221,164)\"],[0.4,\"rgb(230,245,152)\"],[0.5,\"rgb(255,255,191)\"],[0.6,\"rgb(254,224,139)\"],[0.7,\"rgb(253,174,97)\"],[0.8,\"rgb(244,109,67)\"],[0.9,\"rgb(213,62,79)\"],[1.0,\"rgb(158,1,66)\"]]},\"geo\":{\"center\":{},\"domain\":{\"x\":[0.0,1.0],\"y\":[0.0,1.0]},\"scope\":\"usa\"},\"height\":500,\"legend\":{\"tracegroupgap\":0},\"margin\":{\"l\":5,\"r\":10},\"template\":{\"data\":{\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"title\":{\"text\":\"Major Depressive Episode Among Children Ages 12-17 in 2016\"},\"width\":700},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('cfc02413-ceeb-4a96-8a3e-0b425ab1fd8c');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Heat Map\n",
    "depressive_2016['Code'] = depressive_2016['State'].map(code)\n",
    "depressive_fig = px.choropleth(depressive_2016,\n",
    "                    locations='Code',\n",
    "                    color= depressive_2016['12-17 Estimate'].astype(float),\n",
    "#                     range_color=[1,3],\n",
    "                    color_continuous_scale='spectral_r',\n",
    "                    hover_name='State',\n",
    "                    locationmode='USA-states',\n",
    "                    range_color=[9,16],\n",
    "                    title=\"Major Depressive Episode Among Children Ages 12-17 in 2016\",\n",
    "                    scope='usa',\n",
    "                    width=700,\n",
    "                    height=500,\n",
    "                   )\n",
    "depressive_fig.update_layout(coloraxis_colorbar=dict(\n",
    "    title=\"% of Children\"))\n",
    "depressive_fig= depressive_fig.update_layout(margin_l=5)\n",
    "depressive_fig= depressive_fig.update_layout(margin_r=10)\n",
    "depressive_fig"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "6daf0d0d-b016-44cb-8bda-085b780e1fcc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-0.1276872003045753"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "alc_fin_corr= finance_2016[\"TOTAL_REVENUE\"].astype(float).corr(alcoholism_2016[\"12-17 Estimate\"].astype(float), method='pearson')\n",
    "alc_fin_corr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "bc4983f5-15a0-42e9-a6cc-1930e85085a7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>12-17 Estimate</th>\n",
       "      <th>total_revenue</th>\n",
       "      <th>state</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1.67</td>\n",
       "      <td>7498567</td>\n",
       "      <td>Alabama</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2.59</td>\n",
       "      <td>2494691</td>\n",
       "      <td>Alaska</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2.28</td>\n",
       "      <td>8503034</td>\n",
       "      <td>Arizona</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2.14</td>\n",
       "      <td>5401016</td>\n",
       "      <td>Arkansas</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2.33</td>\n",
       "      <td>89217262</td>\n",
       "      <td>California</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  12-17 Estimate  total_revenue       state\n",
       "0           1.67        7498567     Alabama\n",
       "1           2.59        2494691      Alaska\n",
       "2           2.28        8503034     Arizona\n",
       "3           2.14        5401016    Arkansas\n",
       "4           2.33       89217262  California"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "fin_alc=pd.DataFrame(alcoholism_2016[\"12-17 Estimate\"])\n",
    "fin_alc[\"total_revenue\"]=finance_2016[\"TOTAL_REVENUE\"]\n",
    "fin_alc[\"state\"]=alcoholism_2016[\"State\"]\n",
    "fin_alc.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "1a7b937c-9f68-4f61-ad89-33331d6b089f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "customdata": [
          [
           "Alabama"
          ],
          [
           "Alaska"
          ],
          [
           "Arizona"
          ],
          [
           "Arkansas"
          ],
          [
           "California"
          ],
          [
           "Colorado"
          ],
          [
           "Connecticut"
          ],
          [
           "Delaware"
          ],
          [
           "District of Columbia"
          ],
          [
           "Florida"
          ],
          [
           "Georgia"
          ],
          [
           "Hawaii"
          ],
          [
           "Idaho"
          ],
          [
           "Illinois"
          ],
          [
           "Indiana"
          ],
          [
           "Iowa"
          ],
          [
           "Kansas"
          ],
          [
           "Kentucky"
          ],
          [
           "Louisiana"
          ],
          [
           "Maine"
          ],
          [
           "Maryland"
          ],
          [
           "Massachusetts"
          ],
          [
           "Michigan"
          ],
          [
           "Minnesota"
          ],
          [
           "Mississippi"
          ],
          [
           "Missouri"
          ],
          [
           "Montana"
          ],
          [
           "Nebraska"
          ],
          [
           "Nevada"
          ],
          [
           "New Hampshire"
          ],
          [
           "New Jersey"
          ],
          [
           "New Mexico"
          ],
          [
           "New York"
          ],
          [
           "North Carolina"
          ],
          [
           "North Dakota"
          ],
          [
           "Ohio"
          ],
          [
           "Oklahoma"
          ],
          [
           "Oregon"
          ],
          [
           "Pennsylvania"
          ],
          [
           "Rhode Island"
          ],
          [
           "South Carolina"
          ],
          [
           "South Dakota"
          ],
          [
           "Tennessee"
          ],
          [
           "Texas"
          ],
          [
           "Utah"
          ],
          [
           "Vermont"
          ],
          [
           "Virginia"
          ],
          [
           "Washington"
          ],
          [
           "West Virginia"
          ],
          [
           "Wisconsin"
          ],
          [
           "Wyoming"
          ]
         ],
         "hovertemplate": "% of Children 12-17 with Alcoholism=%{x}<br>Total Revenue in USD=%{y}<br>state=%{customdata[0]}<extra></extra>",
         "legendgroup": "",
         "marker": {
          "color": "#636efa",
          "symbol": "circle"
         },
         "mode": "markers",
         "name": "",
         "orientation": "v",
         "showlegend": false,
         "type": "scatter",
         "x": [
          "1.67",
          "2.59",
          "2.28",
          "2.14",
          "2.33",
          "2.60",
          "2.82",
          "2.08",
          "1.88",
          "2.20",
          "1.73",
          "2.35",
          "2.56",
          "2.25",
          "2.07",
          "2.46",
          "2.36",
          "2.08",
          "2.60",
          "2.42",
          "1.99",
          "2.56",
          "2.36",
          "2.16",
          "1.68",
          "2.21",
          "2.91",
          "2.43",
          "2.59",
          "2.28",
          "2.19",
          "2.76",
          "2.21",
          "1.62",
          "2.82",
          "2.16",
          "2.09",
          "2.79",
          "2.12",
          "2.32",
          "2.11",
          "2.87",
          "1.85",
          "2.38",
          "1.87",
          "2.60",
          "2.08",
          "2.30",
          "2.14",
          "2.63",
          "2.86"
         ],
         "xaxis": "x",
         "y": [
          7498567,
          2494691,
          8503034,
          5401016,
          89217262,
          10123271,
          11419673,
          2043577,
          1329719,
          28125598,
          19403453,
          3030519,
          2266490,
          32908958,
          12732161,
          6919477,
          6069563,
          7745928,
          8397136,
          2845391,
          14409321,
          17484704,
          19416061,
          12186135,
          4755399,
          10893231,
          1800909,
          4398811,
          4482886,
          3150473,
          30012666,
          3765069,
          66912661,
          13448045,
          1788749,
          23766529,
          6103728,
          7418055,
          31077289,
          2401541,
          9161667,
          1455737,
          9585331,
          58284155,
          4952923,
          2112365,
          16259274,
          14964364,
          3391579,
          11697466,
          2044669
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "height": 500,
        "legend": {
         "tracegroupgap": 0
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Total School Revenue vs. % of Children with AUD"
        },
        "width": 1000,
        "xaxis": {
         "anchor": "y",
         "autorange": true,
         "domain": [
          0,
          1
         ],
         "range": [
          -2.3226452905811623,
          40.322645290581164
         ],
         "title": {
          "text": "% of Children 12-17 with Alcoholism"
         },
         "type": "category"
        },
        "yaxis": {
         "anchor": "x",
         "autorange": true,
         "domain": [
          0,
          1
         ],
         "range": [
          -4858441.336007129,
          95405422.33600713
         ],
         "title": {
          "text": "Total Revenue in USD"
         },
         "type": "linear"
        }
       }
      },
      "image/png": "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9QPXAbl2Y2Pv1JdL69eb/ogTTekFYBEESLWZWNdEgEg8DUsIEAkCBAESIgJEgwDx1dMRIBIECAJEk2PG9dbTESCgNBYgK621dObC1b0/v/fB1j4hstJaS9dubDT9MSeW0gvAIgiQajOxrokAkXgalhAgEgQIAiREBIgGAeKrpyNAJAgQBIgmx4zrracjQEBpLEBOnV7dJziu3dhIp06v7vvzSmut6Y85sZReABZBgFSbiXVNBIjE07CEAJEgQBAgISJANAgQXz0dASJBgCBANDlmXG89HQECivltcM9cuLrviBBug3vygwCpNhPrmggQiadhCQEiQYAgQEJEgGgQIL56OgJEggBBgGhyzLjeejoCBBRzAbLSWtt33Q8EyMkPAqTaTKxrIkAknoYlBIgEAYIACREBokGA+OrpCBAJAgQBoskx43rr6QgQUEyuATJ+CszzTomZN0ovAIsgQKrNxLomAkTiaVhCgEgQIAiQEBEgGgSIr56OAJEgQBAgmhwzrreejgABpbEAGb/GR93RHiutNa4BcsKDAKk2E+uaCBCJp2EJASJBgCBAQkSAaBAgvno6AkSCAEGAaHLMuN56OgIElMYCJCW57ofe9rbudrjcBeZkBwFSbSbWNREgEk/DEgJEggBBgISIANEgQHz1dASIBAGCANHkmHG99XQECCgmAmSRKb0ALIIAqTYT65oIEImnYQkBIkGAIEBCRIBoECC+ejoCRIIAQYBocsy43no6AgQUBEhDSi8AiyBAqs3EuiYCROJpWEKASBAgCJAQESAaBIivno4AkSBAECCaHDOut56OAAHF5C4wh2WeT39JCQFyWDwNS7qZWNdEgEg8DUsIEAkCBAESIgJEgwDx1dMRIBIECAJEk2PG9dbTESCgZD0C5L0PtopLkMNkzEprbe/vJi/Ueur0au3te5eWW/vualN6AVgEAVJtJtY1ESAST8MSAkSCAEGAhIgA0SBAfPV0BIgEAYIA0eSYcb31dAQIKNlPgSl1G9znyZczF67ukx4rrbV05sLVvT+fOr2aVlpr6dL69b2vXVq/nlZaawiQGeNpWNLNxLomAkTiaVhCgEgQIAiQEBEgGgSIr56OAJEgQBAgmhwzrreejgABJbsAqbs17ovgzIWr++TFJKdOr+67Y82t23f3iQ39+/HHrkIFATJbPA1LuplY10SASDwNSwgQ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AEGAhJhHgITYTjvtXtpp51gPCBAECAJEgwBBgGhyzLjeejoCBBQESENKLwCLIECqzcS6JgJE4mlYQoBIECAIkBARIBoEiK+ejgCRIEAQIJocM663no4AAQUB0pDSC8AiCJBqM7GuiQCReBqWECASBAgCJEQEiAYB4qunI0AkCBAEiCbHjOutpyNAQEGANKT0ArAIAqTaTKxrIkAknoYlBIgEAYIACREBokGA+OrpCBAJAgQBoskx43rr6QgQUBoLkJPKmQtX912EdaW1duB7VlprU//+1OnV2ou3Li230qnTq3t/Lr0ALIIAqTYT65oIEImnYQkBIkGAIEBCRIBoECC+ejoCRIIAQYBocsy43no6AgSUuRUg45JC/3xp/fren89cuLpPeqy01tKZC1f3ff9Ka23f/3Np/Xpaaa0hQGaMp2FJNxPrmggQiadhCQEiQYAgQEJEgGgQIL56OgJEggBBgGhyzLjeejoCBJS5FSCTqLxQTp1e3Xfqzq3bd/eJDf378aNAlpZb6dqNDQTIjPE0LOlmYl0TASLxNCwhQCQIEARIiAgQDQLEV09HgEgQIAgQTY4Z11tPR4CAsjACZPxojvc+2EpLy6303gdbe38/+TUVIGcuXE2X1q/vBQEyezwNS7qZWNdEgEg8DUs5BMjWdjv9n//USw/es39uESC+BMiDh530wx/3009/jgBBgCBAQkSAhIgACREBokGAIEBmfT3h+CyEALm0fn3fkRxHESD6dZUekwKkPxi5z2A4SqOR/b9lOBql4dD+8Y5GKQ0y1M3xemZ7bofy/C7yc+vlNfv4l8N08X/vp7Pne+ns+V76na/30se/HC7ka+ZtPQyNn9sf/riffufrvb3fhd+72l/c12zEHtYfjNIo02s2pKf7Wg/0dH+vGeuB9VAw0Iy5FyDXbmw8V3bUfW38FBk9CkTrjQuQ337ecZ/Hz3qp0x2Y123vDtJOu29etz8Yps92uuZ1c7yej3a6qTcYmtfdafdTe9f+Nev0Bunx05553cFwlOLjXdOa8fFuGgxH5o/1i6e9tNuze25f/ePu3htezat/bPf72+0P06Mn9uthNErpky9sa3620019T+uhO0g7z2zWw7/8upNWL/YO/C784O9sHuunX+ym4ch+PXz+pJe6ffvn9mmnn5527PtDtz9Inz+x38OGo1H69AvbPeyznd00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",
      "text/html": [
       "<div>                            <div id=\"94839d31-1e8b-4611-b7a2-dc8180c4d12b\" class=\"plotly-graph-div\" style=\"height:500px; width:1000px;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"94839d31-1e8b-4611-b7a2-dc8180c4d12b\")) {                    Plotly.newPlot(                        \"94839d31-1e8b-4611-b7a2-dc8180c4d12b\",                        [{\"customdata\":[[\"Alabama\"],[\"Alaska\"],[\"Arizona\"],[\"Arkansas\"],[\"California\"],[\"Colorado\"],[\"Connecticut\"],[\"Delaware\"],[\"District of Columbia\"],[\"Florida\"],[\"Georgia\"],[\"Hawaii\"],[\"Idaho\"],[\"Illinois\"],[\"Indiana\"],[\"Iowa\"],[\"Kansas\"],[\"Kentucky\"],[\"Louisiana\"],[\"Maine\"],[\"Maryland\"],[\"Massachusetts\"],[\"Michigan\"],[\"Minnesota\"],[\"Mississippi\"],[\"Missouri\"],[\"Montana\"],[\"Nebraska\"],[\"Nevada\"],[\"New Hampshire\"],[\"New Jersey\"],[\"New Mexico\"],[\"New York\"],[\"North Carolina\"],[\"North Dakota\"],[\"Ohio\"],[\"Oklahoma\"],[\"Oregon\"],[\"Pennsylvania\"],[\"Rhode Island\"],[\"South Carolina\"],[\"South Dakota\"],[\"Tennessee\"],[\"Texas\"],[\"Utah\"],[\"Vermont\"],[\"Virginia\"],[\"Washington\"],[\"West Virginia\"],[\"Wisconsin\"],[\"Wyoming\"]],\"hovertemplate\":\"% of Children 12-17 with Alcoholism=%{x}<br>Total Revenue in USD=%{y}<br>state=%{customdata[0]}<extra></extra>\",\"legendgroup\":\"\",\"marker\":{\"color\":\"#636efa\",\"symbol\":\"circle\"},\"mode\":\"markers\",\"name\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"type\":\"scatter\",\"x\":[\"1.67\",\"2.59\",\"2.28\",\"2.14\",\"2.33\",\"2.60\",\"2.82\",\"2.08\",\"1.88\",\"2.20\",\"1.73\",\"2.35\",\"2.56\",\"2.25\",\"2.07\",\"2.46\",\"2.36\",\"2.08\",\"2.60\",\"2.42\",\"1.99\",\"2.56\",\"2.36\",\"2.16\",\"1.68\",\"2.21\",\"2.91\",\"2.43\",\"2.59\",\"2.28\",\"2.19\",\"2.76\",\"2.21\",\"1.62\",\"2.82\",\"2.16\",\"2.09\",\"2.79\",\"2.12\",\"2.32\",\"2.11\",\"2.87\",\"1.85\",\"2.38\",\"1.87\",\"2.60\",\"2.08\",\"2.30\",\"2.14\",\"2.63\",\"2.86\"],\"xaxis\":\"x\",\"y\":[7498567,2494691,8503034,5401016,89217262,10123271,11419673,2043577,1329719,28125598,19403453,3030519,2266490,32908958,12732161,6919477,6069563,7745928,8397136,2845391,14409321,17484704,19416061,12186135,4755399,10893231,1800909,4398811,4482886,3150473,30012666,3765069,66912661,13448045,1788749,23766529,6103728,7418055,31077289,2401541,9161667,1455737,9585331,58284155,4952923,2112365,16259274,14964364,3391579,11697466,2044669],\"yaxis\":\"y\"}],                        {\"height\":500,\"legend\":{\"tracegroupgap\":0},\"template\":{\"data\":{\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"choropleth\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"choropleth\"}],\"contour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"contour\"}],\"contourcarpet\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"contourcarpet\"}],\"heatmap\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmap\"}],\"heatmapgl\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"heatmapgl\"}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"histogram2d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2d\"}],\"histogram2dcontour\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"histogram2dcontour\"}],\"mesh3d\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"type\":\"mesh3d\"}],\"parcoords\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"parcoords\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}],\"scatter\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter\"}],\"scatter3d\":[{\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatter3d\"}],\"scattercarpet\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattercarpet\"}],\"scattergeo\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergeo\"}],\"scattergl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattergl\"}],\"scattermapbox\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scattermapbox\"}],\"scatterpolar\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolar\"}],\"scatterpolargl\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterpolargl\"}],\"scatterternary\":[{\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"type\":\"scatterternary\"}],\"surface\":[{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"type\":\"surface\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}]},\"layout\":{\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"autotypenumbers\":\"strict\",\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]],\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]},\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"geo\":{\"bgcolor\":\"white\",\"lakecolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"showlakes\":true,\"showland\":true,\"subunitcolor\":\"white\"},\"hoverlabel\":{\"align\":\"left\"},\"hovermode\":\"closest\",\"mapbox\":{\"style\":\"light\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"gridwidth\":2,\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\"}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"ternary\":{\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"bgcolor\":\"#E5ECF6\",\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"title\":{\"x\":0.05},\"xaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2},\"yaxis\":{\"automargin\":true,\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"zerolinewidth\":2}}},\"title\":{\"text\":\"Total School Revenue vs. % of Children with AUD\"},\"width\":1000,\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"% of Children 12-17 with Alcoholism\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Total Revenue in USD\"}}},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('94839d31-1e8b-4611-b7a2-dc8180c4d12b');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig= px.scatter(fin_alc,\n",
    "    y=\"total_revenue\",\n",
    "    x=\"12-17 Estimate\",\n",
    "#     yformatter=\"%0f\",\n",
    "#     rot=45,\n",
    "    height=500,\n",
    "    width=1000,\n",
    "    labels={\"total_revenue\":\"Total Revenue in USD\",\"12-17 Estimate\": \"% of Children 12-17 with Alcoholism\"},\n",
    "    hover_data={'state'},\n",
    "#     hover_cols=\"state\",\n",
    "    title=\"Total School Revenue vs. % of Children with AUD\")\n",
    "fig"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "id": "1f5ec6bf-2d01-4ab7-a8e7-a080cbe0ce9c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "263507c3-d21f-4633-bfe1-3205d70b2550",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a36ef621-93e1-4cfc-9923-f9f5cc61290d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "abb3a330-da23-40a2-9dfe-1763686973ce",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
