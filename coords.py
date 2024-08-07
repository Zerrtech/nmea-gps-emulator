from pyproj import Geod

coords = [
(-116.1334996,43.5604711),
(-116.1334399,43.5604713),
(-116.1332456,43.5604736),
(-116.1330544,43.5604799),
(-116.1328679,43.5604926),
(-116.1326887,43.5605169),
(-116.1325178,43.5605552),
(-116.1323586,43.5605982),
(-116.1322132,43.5606601),
(-116.132069,43.560733),
(-116.1319317,43.5608172),
(-116.1318095,43.5609134),
(-116.1317,43.561018),
(-116.1316033,43.5611317),
(-116.1315209,43.5612518),
(-116.1314523,43.5613802),
(-116.1313947,43.5615093),
(-116.1313444,43.5616417),
(-116.1312901,43.5617734),
(-116.1312315,43.561903),
(-116.1311771,43.5620288),
(-116.1311321,43.5621535),
(-116.1311018,43.5622781),
(-116.1310944,43.5624007),
(-116.1311088,43.5625192),
(-116.1311414,43.5626334),
(-116.1311988,43.5627401),
(-116.131275,43.5628405),
(-116.1313718,43.562933),
(-116.1314835,43.5630172),
(-116.1316081,43.5630948),
(-116.1317384,43.5631679),
(-116.1318722,43.5632383),
(-116.1320101,43.5633075),
(-116.1321506,43.5633765),
(-116.1322942,43.5634452),
(-116.1324382,43.5635152),
(-116.1325793,43.5635879),
(-116.1327166,43.5636644),
(-116.1328457,43.5637458),
(-116.132965,43.5638351),
(-116.1330691,43.56393),
(-116.1331563,43.5640256),
(-116.1332266,43.564125),
(-116.1332782,43.5642316),
(-116.1333082,43.5643428),
(-116.1333196,43.5644572),
(-116.1333149,43.5645729),
(-116.133294,43.5646886),
(-116.1332542,43.5648019),
(-116.1331969,43.5649111),
(-116.1331248,43.5650145),
(-116.1330376,43.5651087),
(-116.1329387,43.5651952),
(-116.1328272,43.5652712),
(-116.1327129,43.5653393),
(-116.1325903,43.5654024),
(-116.1324615,43.5654682),
(-116.1323276,43.5655403),
(-116.1321944,43.5656113),
(-116.1320594,43.5656803),
(-116.1319201,43.5657509),
(-116.131781,43.5658229),
(-116.1316462,43.5658928),
(-116.1315099,43.5659638),
(-116.1313778,43.5660308),
(-116.1312445,43.5660987),
(-116.131112,43.5661687),
(-116.1309795,43.56624),
(-116.130843,43.5663071),
(-116.1306986,43.5663661),
# (-116.1305482,43.5664132),
# (-116.1303924,43.5664524),
# (-116.1302324,43.5664844),
# (-116.1300707,43.5665089),
# (-116.1299081,43.5665268),
# (-116.1297445,43.566541),
# (-116.1295764,43.5665404),
# (-116.1294098,43.5665376),
# (-116.1292388,43.5665327),
# (-116.1290633,43.5665293),
# (-116.1288885,43.5665286),
# (-116.1287138,43.5665269),
# (-116.1285377,43.5665243),
# (-116.1283585,43.5665177),
# (-116.1281775,43.5665126),
# (-116.127999,43.5665071),
# (-116.1278233,43.5665013),
# (-116.1276502,43.5664945),
# (-116.1274794,43.5664889),
# (-116.1273118,43.5664824),
# (-116.1271479,43.566476),
# (-116.1269856,43.5664699),
# (-116.1268253,43.5664635),
# (-116.1266656,43.5664562),
# (-116.1265083,43.5664494),
# (-116.1263522,43.5664418),
# (-116.1261971,43.5664349),
# (-116.1260428,43.5664291),
# (-116.1258905,43.5664242),
# (-116.1257354,43.5664145),
# (-116.1255805,43.5664088),
# (-116.1254271,43.5664039),
# (-116.1252672,43.5663964),
# (-116.1251056,43.5663926),
# (-116.124947,43.5663923),
# (-116.1247919,43.5663954),
# (-116.124637,43.5664064),
# (-116.1244821,43.5664262),
# (-116.124332,43.5664514),
# (-116.1241823,43.566487),
# (-116.1240428,43.5665311),
# (-116.1239073,43.5665825),
# (-116.1237743,43.5666425),
# (-116.1236498,43.5667089),
# (-116.1235326,43.5667836),
# (-116.1234217,43.5668635),
# (-116.1233148,43.5669406),
# (-116.1232122,43.5670234),
# (-116.1231114,43.5671049),
# (-116.1230123,43.5671875),
# (-116.1229133,43.5672702),
# (-116.1228151,43.5673522),
# (-116.1227153,43.5674337),
# (-116.1226198,43.5675136),
# (-116.1225283,43.5675922),
# (-116.1224324,43.5676698),
# (-116.1223349,43.5677485),
# (-116.1222386,43.5678279),
# (-116.1221401,43.5679094),
# (-116.1220409,43.5679963),
# (-116.1219427,43.5680816),
# (-116.1218439,43.5681639),
# (-116.1217455,43.5682457),
# (-116.1216467,43.5683276),
# (-116.1215509,43.5684081),
# (-116.1214555,43.5684854),
# (-116.1213611,43.5685616),
# (-116.1212688,43.5686322),
# (-116.1211744,43.5687002),
# (-116.1210844,43.5687661),
# (-116.1210018,43.5688269),
# (-116.1209303,43.5688831),
# (-116.1208714,43.568929),
# (-116.1208319,43.568958),
# (-116.1208088,43.5689724),
# (-116.1207983,43.5689772),
# (-116.1207957,43.5689784),
# (-116.1207725,43.5689881),
# (-116.1207255,43.5689986),
# (-116.1206601,43.5689999),
# (-116.1205919,43.5689836),
# (-116.1205236,43.5689595),
# (-116.1204484,43.5689174),
# (-116.1203675,43.5688676),
# (-116.1202776,43.5688138),
# (-116.1201841,43.5687571),
# (-116.120089,43.5686995),
# (-116.1199888,43.5686406),
# (-116.1198866,43.5685808),
# (-116.1197827,43.5685202),
# (-116.1196767,43.5684584),
# (-116.1195702,43.5683969),
# (-116.1194664,43.5683369),
# (-116.1193651,43.568277),
# (-116.1192659,43.5682183),
# (-116.1191661,43.5681602),
# (-116.1190671,43.5681013),
# (-116.1189691,43.5680444),
# (-116.11887,43.5679874),
# (-116.1187675,43.5679282),
# (-116.1186641,43.5678678),
# (-116.1185594,43.5678063),
# (-116.1184516,43.5677421),
# (-116.1183418,43.5676787),
# (-116.1182302,43.5676146),
# (-116.1181154,43.5675513),
# (-116.118,43.5674887),
# (-116.1178855,43.5674261),
# (-116.117774,43.5673639),
# (-116.117666,43.567302),
# (-116.1175604,43.5672407),
# (-116.1174551,43.5671799),
# (-116.1173486,43.5671182),
# (-116.1172399,43.5670563),
# (-116.1171287,43.5669941),
# (-116.1170173,43.5669316),
# (-116.1169042,43.5668685),
# (-116.1167921,43.5668042),
# (-116.116678,43.5667394),
# (-116.1165634,43.5666732),
# (-116.1164475,43.5666072),
# (-116.1163333,43.5665419),
# (-116.1162186,43.5664767),
# (-116.1161043,43.5664109),
# (-116.1159898,43.5663457),
# (-116.1158764,43.5662804),
# (-116.1157617,43.5662143),
# (-116.1156454,43.5661481),
# (-116.1155298,43.5660819),
# (-116.1154142,43.5660154),
# (-116.1152992,43.5659493),
# (-116.1151833,43.5658823),
# (-116.1150682,43.5658149),
# (-116.1149525,43.565747),
# (-116.1148368,43.5656794),
# (-116.1147194,43.5656112),
# (-116.1146005,43.5655436),
# (-116.1144808,43.5654762),
# (-116.1143606,43.5654088),
# (-116.114241,43.5653406),
# (-116.1141221,43.5652716),
# (-116.1140048,43.5652028),
# (-116.113888,43.5651353),
# (-116.1137711,43.56507),
# (-116.1136583,43.5650039),
# (-116.1135502,43.5649368),
# (-116.1134486,43.5648703),
# (-116.1133479,43.5648061),
# (-116.1132427,43.5647457),
# (-116.1131323,43.5646899),
# (-116.1130177,43.5646377),
# (-116.1128998,43.5645895),
# (-116.1127804,43.5645453),
# (-116.1126617,43.5645046),
# (-116.1125491,43.5644673),
# (-116.1124461,43.5644324),
# (-116.112357,43.5643997),
# (-116.1122889,43.5643663),
# (-116.1122522,43.5643256),
# (-116.1122474,43.5642805),
# (-116.1122686,43.5642397),
# (-116.1123037,43.5642035),
# (-116.1123101,43.5641976),
# (-116.1123472,43.564168),
# (-116.1123986,43.564132),
# (-116.1124609,43.5641005),
# (-116.1125333,43.5640773),
# (-116.1126102,43.5640602),
# (-116.1126888,43.5640435),
# (-116.1127652,43.5640279),
# (-116.1128426,43.5640125),
# (-116.1129151,43.5639991),
# (-116.1129874,43.5639862),
# (-116.1130575,43.5639729),
# (-116.1131255,43.5639609),
# (-116.1131943,43.5639483),
# (-116.1132621,43.5639357),
# (-116.11333,43.5639228),
# (-116.1133959,43.5639089),
# (-116.1134605,43.5638943),
# (-116.1135232,43.5638778),
# (-116.1135854,43.5638602),
# (-116.1136458,43.5638401),
# (-116.1137046,43.5638178),
# (-116.1137636,43.5637959),
# (-116.113813,43.5637714),
# (-116.1138653,43.5637429),
# (-116.1139146,43.5637118),
# (-116.1139606,43.5636788),
# (-116.1139984,43.5636447),
# (-116.1140215,43.5636051),
# (-116.1140249,43.5635645),
# (-116.1140241,43.5635573),
# (-116.1140078,43.5635259),
# (-116.1139872,43.5634878),
# (-116.1139429,43.5634613),
# (-116.1138959,43.5634406),
# (-116.1138425,43.5634236),
# (-116.1138318,43.5634202),
# (-116.1137849,43.5634095),
# (-116.1137277,43.5633939),
# (-116.1136725,43.5633802),
# (-116.1136203,43.5633659),
# (-116.113571,43.5633514),
# (-116.1135217,43.5633389),
# (-116.1134737,43.5633422),
# (-116.1134276,43.563359),
# (-116.1133791,43.5633785),
# (-116.1133393,43.5634169),
# (-116.1133029,43.5634616),
# (-116.1132756,43.5635069),
# (-116.1132495,43.5635544),
# (-116.1132254,43.5636),
# (-116.1132121,43.5636444),
# (-116.1132129,43.5636905),
# (-116.1132193,43.5637416),
# (-116.1132331,43.5637867),
# (-116.11324,43.5638288),
# (-116.1132342,43.5638669),
# (-116.1132117,43.5639003),
# (-116.1131774,43.5639271),
# (-116.1131291,43.563945),
# (-116.1130669,43.563956),
# (-116.1129934,43.5639684),
# (-116.1129151,43.5639836),
# (-116.1128331,43.5640009),
# (-116.1127512,43.5640161),
# (-116.1126698,43.5640317),
# (-116.1125883,43.5640473),
# (-116.1125097,43.5640621),
# (-116.1124432,43.5640872),
# (-116.1123829,43.5641223),
# (-116.1123315,43.5641617),
# (-116.1122882,43.5642039),
# (-116.1122481,43.5642455),
# (-116.1122124,43.564284),
# (-116.1121938,43.5643159),
# (-116.1121904,43.5643454),
# (-116.1121908,43.5643507),
# (-116.1122041,43.5643823),
# (-116.1122395,43.5644244),
# (-116.1122997,43.5644663),
# (-116.1123831,43.5645036),
# (-116.112483,43.5645423),
# (-116.1125901,43.564584),
# (-116.1127074,43.5646295),
# (-116.1128311,43.5646769),
# (-116.1129584,43.5647267),
# (-116.1130885,43.5647803),
# (-116.1132164,43.5648385),
# (-116.1133445,43.5649013),
# (-116.1134702,43.5649665),
# (-116.1135928,43.5650341),
# (-116.1137129,43.5651033),
# (-116.1138303,43.5651715),
# (-116.1139494,43.5652396),
# (-116.1140691,43.5653092),
# (-116.1141882,43.5653782),
# (-116.1143066,43.5654476),
# (-116.1144225,43.565516),
# (-116.1145381,43.5655836),
# (-116.1146524,43.5656487),
# (-116.1147656,43.5657129),
# (-116.1148783,43.5657784),
# (-116.1149906,43.5658443),
# (-116.1151035,43.5659097),
# (-116.1152171,43.5659741),
# (-116.1153296,43.5660391),
# (-116.1154392,43.5661027),
# (-116.1155449,43.5661655),
# (-116.1156503,43.5662275),
# (-116.1157559,43.566288),
# (-116.1158645,43.5663484),
# (-116.1159759,43.566409),
# (-116.1160892,43.56647),
# (-116.1162039,43.5665315),
# (-116.1163188,43.5665945),
# (-116.1164338,43.5666578),
# (-116.1165502,43.5667214),
# (-116.1166664,43.5667866),
# (-116.116783,43.5668539),
# (-116.1168991,43.566922),
# (-116.1170144,43.5669902),
# (-116.1171305,43.5670581),
# (-116.117247,43.5671255),
# (-116.1173639,43.5671932),
# (-116.117482,43.5672607),
# (-116.1176004,43.5673287),
# (-116.11772,43.5673976),
# (-116.1178415,43.5674671),
# (-116.1179638,43.5675372),
# (-116.118085,43.5676065),
# (-116.1182081,43.5676751),
# (-116.1183308,43.5677422),
# (-116.1184525,43.5678099),
# (-116.1185734,43.5678785),
# (-116.1186963,43.5679484),
# (-116.1188216,43.5680196),
# (-116.1189462,43.5680902),
# (-116.1190681,43.5681598),
# (-116.1191871,43.5682295),
# (-116.1193036,43.5682978),
# (-116.1194189,43.5683647),
# (-116.1195346,43.5684312),
# (-116.1196495,43.5684965),
# (-116.1197616,43.5685602),
# (-116.1198708,43.5686221),
# (-116.1199763,43.5686826),
# (-116.1200779,43.5687419),
# (-116.1201765,43.5687983),
# (-116.1202689,43.568853),
# (-116.1203542,43.5689037),
# (-116.1204311,43.5689488),
# (-116.1204977,43.5689867),
# (-116.1205517,43.5690156),
# (-116.1205878,43.5690344),
# (-116.1206046,43.5690435),
# (-116.120606,43.5690444),
# (-116.1206156,43.5690496),
# (-116.12064,43.5690625),
# (-116.1206828,43.5690858),
# (-116.1207403,43.5691183),
# (-116.1208093,43.5691579),
# (-116.1208857,43.569203),
# (-116.1209664,43.5692505),
# (-116.1210526,43.5693003),
# (-116.1211429,43.5693522),
# (-116.1212374,43.5694063),
# (-116.1213354,43.5694624),
# (-116.1214355,43.569521),
# (-116.1215373,43.5695813),
# (-116.1216409,43.5696423),
# (-116.1217467,43.569704),
# (-116.1218549,43.569766),
# (-116.1219661,43.5698289),
# (-116.1220776,43.5698926),
# (-116.1221918,43.5699574),
# (-116.1223058,43.5700215),
# (-116.1224207,43.5700866),
# (-116.1225373,43.5701519),
# (-116.1226556,43.570217),
# (-116.1227761,43.5702831),
# (-116.1228976,43.5703496),
# (-116.1230208,43.5704147),
# (-116.1231479,43.5704788),
# (-116.1232774,43.570542),
# (-116.1234086,43.5706056),
# (-116.1235399,43.5706705),
# (-116.1236728,43.5707358),
# (-116.1238066,43.5708008),
# (-116.1239409,43.5708648),
# (-116.1240743,43.5709272),
# (-116.1242076,43.5709887),
# (-116.1243476,43.5710434),
# (-116.1244929,43.5710884),
# (-116.1246465,43.5711255),
# (-116.1248033,43.5711508),
# (-116.1249643,43.5711654),
# (-116.1251263,43.5711669),
# (-116.1252872,43.571155),
# (-116.1254447,43.571131),
# (-116.1256008,43.5710962),
# (-116.1257529,43.5710504),
# (-116.1258999,43.5709936),
# (-116.1260409,43.5709238),
# (-116.1261819,43.5708521),
# (-116.126307,43.5707621),
# (-116.1264247,43.5706646),
# (-116.1265382,43.5705621),
# (-116.1266523,43.5704597),
# (-116.1267718,43.5703567),
# (-116.1268961,43.570255),
# (-116.1270269,43.5701566),
# (-116.1271596,43.5700613),
# (-116.1272951,43.5699691),
# (-116.1274314,43.5698802),
# (-116.1275696,43.5697943),
# (-116.1277085,43.5697111),
# (-116.1278495,43.5696297),
# (-116.1279934,43.5695522),
# (-116.128141,43.5694812),
# (-116.1282936,43.569417),
# (-116.128449,43.5693617),
# (-116.1286067,43.5693069),
# (-116.1287726,43.5692663),
# (-116.1289404,43.5692339),
# (-116.1291062,43.5692102),
# (-116.1292724,43.5691952),
# (-116.1294374,43.5691868),
# (-116.1295983,43.5691832),
# (-116.1297579,43.5691852),
# (-116.129917,43.5691935),
# (-116.1300754,43.5692091),
# (-116.1302295,43.5692307),
# (-116.1303798,43.5692587),
# (-116.1305287,43.5692933),
# (-116.1306757,43.5693334),
# (-116.1308207,43.5693795),
# (-116.1309634,43.5694305),
# (-116.1311054,43.5694847),
# (-116.1312464,43.5695402),
# (-116.1313874,43.5695971),
# (-116.1315291,43.5696544),
# (-116.1316702,43.569714),
# (-116.1318107,43.5697782),
# (-116.1319475,43.5698462),
# (-116.1320815,43.5699177),
# (-116.1322121,43.5699922),
# (-116.1323435,43.5700671),
# (-116.1324754,43.5701402),
# (-116.1326088,43.5702131),
# (-116.1327433,43.5702848),
# (-116.1328789,43.5703578),
# (-116.1330248,43.5704334),
# (-116.133173,43.570509),
# (-116.1333251,43.5705854),
# (-116.1334794,43.5706619),
# (-116.1336356,43.5707385),
# (-116.1337919,43.570815),
# (-116.1339513,43.5708911),
# (-116.1341097,43.570966),
# (-116.1342693,43.571041),
# (-116.1344303,43.5711163),
# (-116.1345915,43.5711889),
# (-116.1347539,43.5712598),
# (-116.1349144,43.5713302),
# (-116.1350714,43.5714006),
# (-116.1352244,43.5714704),
# (-116.135375,43.5715411),
# (-116.1355251,43.5716128),
# (-116.1356737,43.5716859),
# (-116.135821,43.571759),
# (-116.1359687,43.5718329),
# (-116.1361184,43.5719066),
# (-116.1362671,43.5719804),
# (-116.1364146,43.5720536),
# (-116.1365638,43.5721272),
# (-116.1367107,43.5721992),
# (-116.1368591,43.5722731),
# (-116.1370066,43.5723475),
# (-116.1371535,43.5724213),
# (-116.1373023,43.5724953),
# (-116.1374512,43.5725685),
# (-116.1375988,43.5726413),
# (-116.1377465,43.5727157),
# (-116.1378947,43.5727905),
# (-116.1380441,43.5728658),
# (-116.138194,43.572941),
# (-116.1383441,43.5730151),
# (-116.1384923,43.5730881),
# (-116.1386361,43.5731614),
# (-116.1387721,43.573235),
# (-116.138902,43.573312),
# (-116.1390251,43.5733935),
# (-116.1391401,43.5734798),
# (-116.1392494,43.5735695),
# (-116.1393541,43.5736621),
# (-116.1394538,43.5737552),
# (-116.1395516,43.5738477),
# (-116.1396489,43.5739387),
# (-116.1397444,43.5740295),
# (-116.1398383,43.5741198),
# (-116.1399294,43.5742111),
# (-116.1400177,43.5743035),
# (-116.1401014,43.5743983),
# (-116.1401769,43.5744979),
# (-116.140237,43.5746031),
# (-116.1402827,43.5747121),
# (-116.1403163,43.5748229),
# (-116.1403386,43.574934),
# (-116.1403502,43.5750431),
# (-116.1403526,43.5751514),
# (-116.1403456,43.5752601),
# (-116.1403291,43.5753674),
# (-116.1403017,43.5754726),
# (-116.1402636,43.5755743),
# (-116.1402166,43.5756725),
# (-116.1401648,43.5757697),
# (-116.1401121,43.5758651),
# (-116.1400599,43.5759593),
# (-116.1400115,43.5760466),
# (-116.1399642,43.576125),
# (-116.1399122,43.5761911),
# (-116.1398573,43.5762506),
# (-116.1397828,43.5762898),
# (-116.139704,43.5763218),
# (-116.1396297,43.576357),
# (-116.139575,43.5764024),
# (-116.139546,43.5764591),
# (-116.1395415,43.5765198),
# (-116.1395594,43.5765774),
# (-116.1396078,43.5766259),
# (-116.1396911,43.5766566),
# (-116.1397946,43.5766751),
# (-116.1399122,43.576683),
# (-116.1400368,43.5766934),
# (-116.1401715,43.5767106),
# (-116.1403147,43.5767386),
# (-116.140462,43.5767774),
# (-116.1406154,43.5768266),
# (-116.1407741,43.5768813),
# (-116.1409362,43.5769391),
# (-116.1411009,43.5769963),
# (-116.1412695,43.5770558),
# (-116.1414389,43.5771154),
# (-116.14161,43.5771755),
# (-116.1417816,43.5772361),
# (-116.1419529,43.5772964),
# (-116.1421247,43.5773558),
# (-116.1422936,43.5774158),
# (-116.1424607,43.5774749),
# (-116.142632,43.5775357),
# (-116.1428066,43.5775975),
# (-116.1429815,43.5776574),
# (-116.1431527,43.577717),
# (-116.1433184,43.5777755),
# (-116.1434807,43.5778332),
# (-116.1436453,43.5778913),
# (-116.1438104,43.5779497),
# (-116.1439767,43.5780077),
# (-116.144145,43.5780642),
# (-116.1443129,43.5781161),
# (-116.1444849,43.5781637),
# (-116.1446589,43.578205),
# (-116.1448345,43.57824),
# (-116.1450127,43.5782682),
# (-116.1451925,43.5782893),
# (-116.1453752,43.5783037),
# (-116.1455607,43.5783118),
# (-116.1457474,43.578313),
# (-116.1459351,43.5783072),
# (-116.1461229,43.578295),
# (-116.1463095,43.5782814),
# (-116.1464917,43.578256),
# (-116.1466727,43.5782221),
# (-116.1468518,43.5781802),
# (-116.1470248,43.5781335),
# (-116.1471869,43.578082),
# (-116.1473416,43.5780276),
# (-116.1474938,43.5779714),
# (-116.1476408,43.577909),
# (-116.147792,43.5778437),
# (-116.1479423,43.5777787),
# (-116.148098,43.5777123),
# (-116.1482532,43.5776461),
# (-116.1484064,43.5775769),
# (-116.1485632,43.5775038),
# (-116.1487217,43.5774301),
# (-116.1488803,43.5773562),
# (-116.149039,43.5772826),
# (-116.1491996,43.5772089),
# (-116.1493619,43.5771341),
# (-116.1495226,43.57706),
# (-116.1496851,43.5769852),
# (-116.1498427,43.5769118),
# (-116.1499977,43.5768398),
# (-116.1501502,43.5767692),
# (-116.1502993,43.5766986),
# (-116.1504477,43.576628),
# (-116.1505944,43.5765565),
# (-116.1507411,43.5764862),
# (-116.1508893,43.5764173),
# (-116.1510399,43.5763494),
# (-116.1511925,43.5762795),
# (-116.1513434,43.5762092),
# (-116.1514956,43.5761386),
# (-116.1516506,43.5760679),
# (-116.1518054,43.5759979),
# (-116.1519575,43.5759294),
# (-116.1521092,43.5758607),
# (-116.1522607,43.5757925),
# (-116.1524128,43.5757249),
# (-116.1525677,43.57566),
# (-116.1527234,43.5756033),
# (-116.1528834,43.5755485),
# (-116.1530522,43.5755067),
# (-116.1532251,43.5754736),
# (-116.1533988,43.5754468),
# (-116.1535734,43.5754229),
# (-116.1537491,43.5754039),
# (-116.1539243,43.5753894),
# (-116.1540995,43.5753761),
# (-116.1542695,43.5753713),
# (-116.154438,43.5753752),
# (-116.1546042,43.5753876),
# (-116.1547636,43.575407),
# (-116.1549188,43.5754319),
# (-116.1550725,43.5754618),
# (-116.1552235,43.5754964),
# (-116.1553742,43.5755362),
# (-116.1555222,43.5755814),
# (-116.1556658,43.5756325),
# (-116.1558071,43.5756835),
# (-116.1559418,43.5757445),
# (-116.156073,43.5758127),
# (-116.1561982,43.5758856),
# (-116.1563197,43.5759619),
# (-116.1564415,43.5760389),
# (-116.1565639,43.5761156),
# (-116.1566885,43.5761939),
# (-116.1568143,43.5762747),
# (-116.1569372,43.5763645),
# (-116.1570544,43.5764623),
# (-116.157165,43.5765644),
# (-116.157265,43.576668),
# (-116.1573592,43.5767692),
# (-116.1574535,43.5768673),
# (-116.1575418,43.5769589),
# (-116.1576222,43.5770322),
# (-116.1576819,43.5770899),
# (-116.1577203,43.5771309),
# (-116.1577429,43.5771574),
# (-116.1577551,43.5771719),
# (-116.1577566,43.5771736),
# (-116.1577638,43.5771821),
# (-116.157774,43.5771921),
# (-116.1577829,43.5772015),
# (-116.1577907,43.5772124),
# (-116.1577997,43.5772228),
# (-116.1578013,43.5772246),
# (-116.1578104,43.5772326),
# (-116.1578185,43.5772436),
# (-116.1578419,43.5772613),
# (-116.1578749,43.5772845),
# (-116.1579336,43.5772939),
# (-116.1579452,43.5772945),
# (-116.1580034,43.5772831),
# (-116.1580791,43.5772667),
# (-116.158151,43.5772292),
# (-116.1582239,43.577188),
# (-116.1582937,43.5771449),
# (-116.1583582,43.5771034),
# (-116.1584225,43.5770652),
# (-116.1584862,43.5770285),
# (-116.1585488,43.5769938),
# (-116.1586106,43.5769604),
# (-116.1586747,43.5769271),
# (-116.1587445,43.5768964),
# (-116.1588121,43.5768676),
# (-116.1588801,43.5768422),
# (-116.1589648,43.5768276),
# (-116.1590501,43.5768243),
# (-116.15913,43.5768275),
# (-116.1592066,43.5768384),
# (-116.1592784,43.5768587),
# (-116.1593492,43.5768862),
# (-116.159418,43.5769217),
# (-116.1594831,43.5769625),
# (-116.159542,43.5770081),
# (-116.1595926,43.5770555),
# (-116.1596337,43.5771096),
# (-116.15967,43.5771633),
# (-116.1596939,43.5772212),
# (-116.1596989,43.5772926),
# (-116.1597001,43.577368),
# (-116.1596978,43.5774469),
# (-116.159695,43.5775253),
# (-116.1596909,43.577603),
# (-116.159688,43.5776796),
# (-116.1596906,43.5777491),
# (-116.1597085,43.577819),
# (-116.1597391,43.5778895),
# (-116.1597857,43.577956),
# (-116.1598407,43.5780143),
# (-116.1598987,43.5780741),
# (-116.1599556,43.5781341),
# (-116.1600123,43.5781966),
# (-116.1600703,43.5782611),
# (-116.1601297,43.5783251),
# (-116.1601933,43.578384),
# (-116.1602606,43.5784407),
# (-116.1603314,43.5784955),
# (-116.1604073,43.5785482),
# (-116.160488,43.5785991),
# (-116.1605737,43.5786484),
# (-116.1606629,43.5786939),
# (-116.1607553,43.5787351),
# (-116.1608468,43.5787749),
# (-116.1609404,43.5788087),
# (-116.16103,43.5788451),
# (-116.1611187,43.5788811),
# (-116.1612124,43.5789147),
# (-116.1613057,43.5789513),
# (-116.1613942,43.5789889),
# (-116.1614826,43.5790238),
# (-116.1615717,43.5790586),
# (-116.1616619,43.5790942),
# (-116.1617519,43.5791304),
# (-116.1618418,43.5791667),
# (-116.1619291,43.5792046),
# (-116.1620156,43.5792447),
# (-116.1621013,43.5792869),
# (-116.1621887,43.5793306),
# (-116.1622741,43.579375),
# (-116.1623555,43.5794191),
# (-116.1624337,43.5794637),
# (-116.1625103,43.5795086),
# (-116.1625861,43.5795542),
# (-116.1626656,43.5796028),
# (-116.1627433,43.579651),
# (-116.1628207,43.5796993),
# (-116.1628988,43.5797502),
# (-116.1629767,43.5798),
# (-116.1630554,43.5798499),
# (-116.1631322,43.5798978),
# (-116.1632038,43.5799449),
# (-116.1632661,43.579985),
# (-116.163317,43.5800171),
# (-116.1633508,43.5800397),
# (-116.1633743,43.5800525),
# (-116.1633785,43.5800543),
# (-116.1634018,43.5800589),
# (-116.1634484,43.580061),
# (-116.1635092,43.5800504),
# (-116.1635713,43.5800236),
# (-116.1636244,43.5799836),
# (-116.1636738,43.5799431),
# (-116.1637143,43.5798922),
# (-116.1637494,43.5798398),
# (-116.1637806,43.5797877),
# (-116.1638075,43.5797392),
# (-116.1638319,43.5796904),
# (-116.1638576,43.579627),
# (-116.1638785,43.5795606),
# (-116.1638984,43.5794947),
# (-116.1639195,43.5794283),
# (-116.1639329,43.5793574),
# (-116.1639412,43.5792849),
# (-116.1639302,43.5792116),
# (-116.1639082,43.5791383),
# (-116.1638632,43.579064),
# (-116.1638172,43.5789869),
# (-116.1637726,43.5789076),
# (-116.1637328,43.578828),
# (-116.1636984,43.5787508),
# (-116.1636715,43.5786725),
# (-116.1636489,43.5786016),
# (-116.163631,43.5785351),
# (-116.1636187,43.5784807),
# (-116.1636117,43.5784233),
# (-116.1636149,43.5783538),
# (-116.1636284,43.5782713),
# (-116.1636532,43.5781795),
# (-116.1636863,43.5780875),
# (-116.1637289,43.5780003),
# (-116.1637767,43.5779154),
# (-116.1638238,43.5778321),
# (-116.1638714,43.5777492),
# (-116.1639167,43.577672),
# (-116.1639566,43.5775989),
# (-116.1639841,43.5775343),
# (-116.1640081,43.5774714),
# (-116.1640232,43.5774158),
# (-116.1640369,43.5773576),
# (-116.1640519,43.5772865),
# (-116.1640432,43.5772044),
# (-116.1640248,43.5771192),
# (-116.1639996,43.5770332),
# (-116.1639779,43.5769479),
# (-116.1639678,43.5768696),
# (-116.1639648,43.5767913),
# (-116.1639611,43.5767151),
# (-116.1639603,43.5766393),
# (-116.1639593,43.5765657),
# (-116.1639565,43.5764989),
# (-116.163956,43.5764377),
# (-116.1639564,43.5763803),
# (-116.1639585,43.5763144),
# (-116.1639546,43.5762418),
# (-116.1639331,43.576169),
# (-116.1638888,43.5761007),
# (-116.1638267,43.57604),
# (-116.1637481,43.5759904),
# (-116.1636615,43.57595),
# (-116.1635825,43.5759077),
# (-116.1635067,43.5758636),
# (-116.1634541,43.5758099),
# (-116.1634348,43.575746),
# (-116.1634296,43.5756749),
# (-116.1634246,43.5756063),
# (-116.1634267,43.5755374),
# (-116.1634304,43.5754647),
# (-116.163435,43.5753938),
# (-116.1634419,43.5753223),
# (-116.1634459,43.5752458),
# (-116.1634456,43.5751632),
# (-116.1634477,43.5750795),
# (-116.163452,43.5749957),
# (-116.1634588,43.5749112),
# (-116.163466,43.574829),
# (-116.1634724,43.574749),
# (-116.1634804,43.5746717),
# (-116.1634868,43.5745983),
# (-116.1634928,43.574527),
# (-116.1634967,43.5744576),
# (-116.1634984,43.57439),
# (-116.1634988,43.5743314),
# (-116.1634998,43.5742857),
# (-116.1635003,43.5742555),
# (-116.1635011,43.5742406),
# (-116.1635012,43.574239),
# (-116.1635013,43.5742415),
# (-116.1634998,43.5742262),
# (-116.1634996,43.5741977),
# (-116.1634968,43.5741577),
# (-116.1634939,43.5741101),
# (-116.1634912,43.574056),
# (-116.1634886,43.5739968),
# (-116.1634854,43.573933),
# (-116.163481,43.5738665),
# (-116.1634764,43.5737999),
# (-116.1634713,43.5737346),
# (-116.1634672,43.5736697),
# (-116.1634637,43.573606),
# (-116.1634596,43.5735439),
# (-116.1634557,43.5734824),
# (-116.163451,43.573421),
# (-116.1634473,43.5733603),
# (-116.1634441,43.5732998),
# (-116.1634402,43.5732367),
# (-116.1634361,43.5731713),
# (-116.1634315,43.5731062),
# (-116.1634273,43.573043),
# (-116.1634237,43.5729813),
# (-116.1634217,43.5729192),
# (-116.1634223,43.5728537),
# (-116.1634252,43.5727848),
# (-116.1634292,43.5727138),
# (-116.1634336,43.5726416),
# (-116.1634374,43.5725698),
# (-116.1634399,43.5724999),
# (-116.1634424,43.5724314),
# (-116.1634444,43.5723648),
# (-116.1634466,43.5722996),
# (-116.1634495,43.5722337),
# (-116.1634517,43.5721651),
# (-116.1634538,43.5720931),
# (-116.1634562,43.572021),
# (-116.1634588,43.5719506),
# (-116.1634611,43.5718793),
# (-116.1634632,43.5718074),
# (-116.163466,43.5717342),
# (-116.1634682,43.571662),
# (-116.1634694,43.5715888),
# (-116.1634702,43.5715164),
# (-116.16347,43.5714453),
# (-116.1634685,43.5713762),
# (-116.163468,43.571308),
# (-116.1634668,43.5712406),
# (-116.1634667,43.5711738),
# (-116.1634678,43.5711073),
# (-116.1634693,43.5710392),
# (-116.1634695,43.5709666),
# (-116.1634697,43.5708894),
# (-116.163468,43.5708078),
# (-116.1634664,43.5707251),
# (-116.163466,43.570643),
# (-116.1634653,43.5705589),
# (-116.1634656,43.5704759),
# (-116.1634658,43.5703919),
# (-116.1634669,43.5703064),
# (-116.1634663,43.5702197),
# (-116.1634665,43.570132),
# (-116.1634669,43.5700449),
# (-116.1634665,43.5699567),
# (-116.1634665,43.5698686),
# (-116.1634666,43.5697822),
# (-116.1634659,43.569697),
# (-116.1634669,43.569613),
# (-116.1634675,43.569531),
# (-116.1634679,43.5694506),
# (-116.1634674,43.5693717),
# (-116.1634665,43.5692952),
# (-116.1634663,43.5692189),
# (-116.1634685,43.5691386),
# (-116.1634705,43.5690529),
# (-116.1634711,43.5689639),
# (-116.1634701,43.5688734),
# (-116.1634687,43.5687817),
# (-116.1634673,43.5686905),
# (-116.1634654,43.568601),
# (-116.1634634,43.5685142),
# (-116.1634627,43.5684286),
# (-116.1634634,43.5683452),
# (-116.1634666,43.5682633),
# (-116.1634714,43.5681838),
# (-116.163476,43.568109),
# (-116.1634773,43.5680402),
# (-116.1634771,43.5679816),
# (-116.1634778,43.5679376),
# (-116.1634811,43.5679112),
# (-116.1634868,43.5678961),
# (-116.1634881,43.5678935),
# (-116.1634965,43.5678803),
# (-116.1635104,43.5678569),
# (-116.1635519,43.5678324),
# (-116.1636156,43.5678179),
# (-116.1637021,43.5678116),
# (-116.1638068,43.5678132),
# (-116.1639276,43.567818),
# (-116.1640602,43.5678224),
# (-116.1641914,43.5678264),
# (-116.1643234,43.5678289),
# (-116.1644576,43.5678299),
# (-116.1645952,43.5678287),
# (-116.1647361,43.5678273),
# (-116.1648797,43.5678274),
# (-116.1650243,43.5678277),
# (-116.1651717,43.5678283),
# (-116.1653191,43.5678277),
# (-116.1654675,43.5678269),
# (-116.1656162,43.5678264),
# (-116.1657664,43.5678268),
# (-116.1659162,43.5678268),
# (-116.1660657,43.5678288),
# (-116.1662164,43.5678297),
# (-116.1663674,43.5678304),
# (-116.1665172,43.5678304),
# (-116.1666642,43.5678303),
# (-116.1668068,43.5678295),
# (-116.1669486,43.5678281),
# (-116.1670903,43.5678253),
# (-116.1672319,43.5678211),
# (-116.167373,43.5678176),
# (-116.1675143,43.5678161),
# (-116.1676578,43.5678151),
# (-116.1678034,43.5678145),
# (-116.167951,43.5678141),
# (-116.1680984,43.5678143),
# (-116.1682459,43.5678149),
# (-116.1683918,43.5678161),
# (-116.1685366,43.5678179),
# (-116.1686814,43.567821),
# (-116.1688282,43.5678245),
# (-116.1689749,43.5678273),
# (-116.169121,43.56783),
# (-116.1692694,43.5678324),
# (-116.1694185,43.567834),
# (-116.1695686,43.5678359),
# (-116.1697205,43.5678372),
# (-116.1698726,43.5678383),
# (-116.1700231,43.5678385),
# (-116.1701749,43.5678381),
# (-116.1703266,43.5678369),
# (-116.1704785,43.5678359),
# (-116.1706294,43.5678352),
# (-116.1707777,43.5678336),
# (-116.1709228,43.5678303),
# (-116.1710678,43.5678272),
# (-116.1712119,43.5678246),
# (-116.171356,43.5678232),
# (-116.1714986,43.5678237),
# (-116.1716434,43.5678248),
# (-116.1717884,43.5678253),
# (-116.1719347,43.5678255),
# (-116.1720835,43.5678256),
# (-116.1722335,43.5678269),
# (-116.1723905,43.5678297),
# (-116.1725523,43.5678353),
# (-116.1727174,43.5678393),
# (-116.1728843,43.5678422),
# (-116.1730466,43.5678458),
# (-116.1732022,43.5678491),
# (-116.1733547,43.5678525),
# (-116.173508,43.567855),
# (-116.1736663,43.5678561),
# (-116.1738295,43.5678565),
# (-116.1739936,43.567857),
# (-116.1741608,43.5678585),
# (-116.1743283,43.56786),
# (-116.1744934,43.5678607),
# (-116.1746585,43.5678615),
# (-116.174824,43.567863),
# (-116.1749884,43.5678654),
# (-116.1751496,43.5678683),
# (-116.1753075,43.5678706),
# (-116.1754651,43.5678717),
# (-116.1756223,43.5678731),
# (-116.1757802,43.5678742),
# (-116.175937,43.5678754),
# (-116.1760919,43.5678764),
# (-116.1762483,43.5678765),
# (-116.1764048,43.5678763),
# (-116.176558,43.5678751),
# (-116.1767079,43.5678744),
# (-116.1768542,43.5678735),
# (-116.176995,43.5678727),
# (-116.177129,43.5678723),
# (-116.1772468,43.5678723),
# (-116.1773448,43.5678753),
# (-116.1774233,43.5678885),
# (-116.1774797,43.5679184),
# (-116.1775186,43.5679594),
# (-116.1775232,43.5680167),
# (-116.1775204,43.5680817),
# (-116.1775173,43.5681585),
# (-116.1775175,43.5682415),
# (-116.177526,43.5683265),
# (-116.1775492,43.5684144),
# (-116.1775843,43.5685013),
# (-116.177625,43.5685873),
# (-116.1776737,43.5686747),
# (-116.1777461,43.5687639),
# (-116.1778407,43.5688516),
# (-116.1779481,43.5689339),
# (-116.1780637,43.5690094),
# (-116.178188,43.5690773),
# (-116.1783231,43.5691343),
# (-116.1784649,43.5691824),
# (-116.1786116,43.5692246),
# (-116.1787669,43.569252),
# (-116.178925,43.5692696),
# (-116.1790804,43.5692825),
# (-116.1792339,43.569295),
# (-116.1793887,43.5693078),
# (-116.1795428,43.5693202),
# (-116.1796982,43.5693334),
# (-116.1798551,43.5693459),
# (-116.1800133,43.5693585),
# (-116.1801737,43.5693713),
# (-116.180336,43.5693838),
# (-116.1805007,43.5693976),
# (-116.1806645,43.5694122),
# (-116.1808277,43.5694265),
# (-116.1809922,43.5694401),
# (-116.1811548,43.5694539),
# (-116.1813166,43.5694674),
# (-116.1814748,43.5694876),
# (-116.1816307,43.5695179),
# (-116.1817833,43.5695607),
# (-116.1819265,43.5696179),
# (-116.1820628,43.5696846),
# (-116.182193,43.5697574),
# (-116.1823192,43.5698351),
# (-116.1824447,43.5699161),
# (-116.182571,43.5699968),
# (-116.1826943,43.5700805),
# (-116.1828068,43.5701656),
# (-116.182903,43.5702468),
# (-116.1829854,43.5703239),
# (-116.1830579,43.5704016),
# (-116.1831289,43.5704861),
# (-116.1831997,43.5705785),
# (-116.1832696,43.5706745),
# (-116.1833317,43.5707728),
# (-116.1833822,43.5708773),
# (-116.1834305,43.5709855),
# (-116.183464,43.5711003),
# (-116.183487,43.5712141),
# (-116.1835,43.5713282),
# (-116.1835047,43.5714405),
# (-116.1835098,43.5715521),
# (-116.1835088,43.57166),
# (-116.1835046,43.5717708),
# (-116.1835019,43.5718859),
# (-116.1835002,43.5720032),
# (-116.1834994,43.5721174),
# (-116.1834993,43.5722298),
# (-116.1834988,43.5723427),
# (-116.1834983,43.5724583),
# (-116.1834984,43.5725758),
# (-116.1834934,43.5726951),
# (-116.1834897,43.5728197),
# (-116.1834889,43.5729437),
# (-116.1834893,43.5730699),
# (-116.1834914,43.5731932),
# (-116.1834921,43.5733192),
# (-116.1834916,43.5734456),
# (-116.1834914,43.573571),
# (-116.1834919,43.5736937),
# (-116.183492,43.5738151),
# (-116.1834919,43.5739409),
# (-116.1834917,43.5740668),
# (-116.1834909,43.5741905),
# (-116.1834872,43.5743099),
# (-116.1834837,43.5744307),
# (-116.1834827,43.5745529),
# (-116.1834834,43.5746744),
# (-116.1834861,43.574799),
# (-116.1834869,43.5749196),
# (-116.1834851,43.575038),
# (-116.1834863,43.5751561),
# (-116.183487,43.5752749),
# (-116.1834846,43.5753894),
# (-116.1834825,43.5755017),
# (-116.1834803,43.5756116),
# (-116.183479,43.5757257),
# (-116.1834774,43.5758376),
# (-116.1834785,43.5759455),
# (-116.1834779,43.5760574),
# (-116.183477,43.5761678),
# (-116.1834723,43.5762791),
# (-116.1834708,43.5763893),
# (-116.1834689,43.5765025),
# (-116.1834681,43.5766155),
# (-116.1834668,43.5767301),
# (-116.1834672,43.5768454),
# (-116.1834675,43.5769613),
# (-116.1834691,43.5770762),
# (-116.1834693,43.577192),
# (-116.1834695,43.5773073),
# (-116.1834696,43.5774241),
# (-116.1834694,43.5775388),
# (-116.1834689,43.5776506),
# (-116.183467,43.5777607),
# (-116.183465,43.577868),
# (-116.1834628,43.5779734),
# (-116.1834597,43.5780784),
# (-116.1834558,43.5781821),
# (-116.1834539,43.5782842),
# (-116.1834534,43.5783584),
]

def get_hs():
    g = Geod(ellps='WGS84')
    hs = []
    for ci in range(len(coords)-1):
        prev = coords[ci]
        curr = coords[ci+1]
        # print("prev:", prev, " curr:", curr)
        plon = prev[0]
        plat = prev[1]
        clon = curr[0]
        clat = curr[1]
        out = g.inv(plon, plat, clon, clat)
        # print(out)
        # find distace between points
        # find heading between points
        speed = out[2] * 1.943844 * 0.75
        heading = out[0]
        heading = (out[0] + 360) % 360
        hs.append((heading, speed))
        print("speed knots:", speed, " mph:", (out[2] * 0.000621371) * 3600, " heading:", heading)
    return hs

def get_hs_back():
    point_secs = 0.8
    g = Geod(ellps='WGS84')
    hs = []
    for ci in range(len(coords)-1):
        prev = coords[ci]
        curr = coords[ci+1]
        # print("prev:", prev, " curr:", curr)
        plon = prev[0]
        plat = prev[1]
        clon = curr[0]
        clat = curr[1]
        out = g.inv(plon, plat, clon, clat)
        # print(out)
        # find distace between points
        # find heading between points
        speed = (out[2] / point_secs) * 1.943844
        heading = out[0]
        heading = (out[0] + 360) % 360
        hs.append((heading, speed))
        print("i:", ci, " speed knots:", speed, " mph:", (out[2] * 0.000621371) * 3600, " heading:", heading)
    for ci in range(len(coords)-1):
        prev = coords[len(coords)-1 - ci]
        curr = coords[len(coords)-1 - ci-1]
        # print("prev:", prev, " curr:", curr)
        plon = prev[0]
        plat = prev[1]
        clon = curr[0]
        clat = curr[1]
        out = g.inv(plon, plat, clon, clat)
        # print(out)
        # find distace between points
        # find heading between points
        speed = (out[2] / point_secs) * 1.943844
        heading = out[0]
        heading = (out[0] + 360) % 360
        hs.append((heading, speed))
        print("i:", ci, " speed knots:", speed, " mph:", (out[2] * 0.000621371) * 3600, " heading:", heading)        
    return hs    

if __name__ == '__main__':
    get_hs()