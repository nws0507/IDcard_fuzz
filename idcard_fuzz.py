#! /usr/bin/env python
# coding=utf-8
# @Author: nws0507
import time
import datetime
import re

# 1-6位地区编码
area = ['451381', '542336', '320902', '321324', '210900', '511132', '320682', '222400', '411023', '420922', '511324',
        '320982', '542300', '140881', '542429', '632700', '370982', '341000', '130433', '211324', '130700', '150428',
        '230422', '330303', '331002', '231002', '350203', '659002', '320804', '320411', '141102', '450404', '341523',
        '130922', '210503', '350105', '620924', '421222', '330226', '620802', '320203', '451227', '532600', '440600',
        '530400', '371402', '522731', '621021', '500119', '152502', '320402', '370781', '410800', '340721', '620503',
        '610402', '231200', '231085', '331100', '140922', '440982', '320602', '130625', '140221', '220500', '230223',
        '451322', '321281', '360803', '410802', '640402', '211422', '341800', '341122', '430502', '320508', '542323',
        '431125', '330104', '440184', '340303', '130123', '370983', '371581', '441200', '141030', '130302', '370100',
        '131026', '130823', '511800', '371302', '532929', '330703', '430321', '621226', '230382', '510812', '371122',
        '622921', '520203', '150525', '511381', '421381', '211011', '211202', '370304', '500223', '130703', '150105',
        '130322', '421121', '511423', '430524', '522301', '420203', '341323', '542622', '542226', '511323', '140926',
        '130404', '530622', '320600', '421003', '440607', '230716', '530800', '230804', '230900', '150303', '610424',
        '130828', '620921', '330700', '420322', '610702', '330302', '610431', '620402', '532528', '511322', '220503',
        '430702', '130727', '620423', '370402', '530827', '632223', '230300', '610581', '451224', '440523', '632822',
        '210922', '350322', '360922', '140581', '350925', '370404', '140729', '411282', '440106', '411200', '361124',
        '230307', '450681', '230112', '341021', '321000', '320826', '210103', '632121', '230403', '130702', '520421',
        '621228', '210782', '410212', '611000', '500226', '330803', '622925', '230111', '422825', '532930', '130127',
        '513401', '511421', '511723', '513336', '510522', '410000', '623025', '130303', '320583', '652300', '360429',
        '210603', '430422', '150121', '440204', '331023', '430304', '140200', '230229', '320829', '341322', '621000',
        '420000', '520201', '150204', '542428', '640381', '421024', '130000', '451026', '610527', '640000', '532628',
        '430525', '520326', '150783', '360000', '542335', '152523', '421223', '320114', '440608', '130902', '430703',
        '360727', '321323', '522327', '522634', '340300', '411702', '371325', '611025', '370303', '230302', '610330',
        '370000', '371000', '150927', '341721', '410323', '370305', '411721', '510824', '431382', '340702', '410204',
        '370214', '110228', '440783', '230407', '140107', '440308', '230100', '510112', '131123', '230184', '210404',
        '469032', '130200', '532624', '542523', '450300', '140181', '450800', '510504', '131126', '542621', '110107',
        '211403', '331004', '411330', '320115', '211421', '320830', '130108', '130705', '430822', '451022', '440282',
        '341222', '210422', '440511', '421300', '140822', '440304', '120221', '410326', '511826', '520329', '610426',
        '513422', '211004', '441821', '411625', '370302', '440781', '510703', '361128', '430603', '610423', '150702',
        '320102', '210311', '411426', '500238', '450311', '420704', '511526', '610300', '410422', '340311', '140623',
        '510300', '130821', '140224', '410927', '350212', '130131', '152528', '542527', '520181', '510411', '350124',
        '130582', '440923', '370828', '330182', '411522', '500105', '330204', '440804', '330000', '610427', '360300',
        '110111', '211122', '130981', '331022', '150522', '360105', '610116', '410403', '230602', '150122', '610625',
        '341723', '440222', '530723', '513435', '341321', '520221', '410581', '520603', '320800', '500108', '330782',
        '632824', '440200', '620825', '421224', '150426', '451223', '510122', '410621', '220821', '130400', '510781',
        '530921', '150800', '330206', '130983', '340406', '140227', '500113', '513224', '542333', '131003', '330424',
        '420204', '331121', '542427', '222404', '130223', '321003', '440103', '450105', '341102', '410505', '530328',
        '410600', '130283', '532526', '110000', '371326', '230882', '210213', '110116', '130125', '330211', '632802',
        '141022', '130535', '445222', '141027', '450127', '130635', '130921', '513423', '511525', '130406', '150221',
        '510106', '430412', '542227', '411621', '210203', '710000', '441581', '522725', '410882', '210600', '630122',
        '140827', '530621', '410803', '451323', '610102', '440400', '350430', '410304', '542132', '522324', '370322',
        '620302', '520627', '232722', '533324', '350725', '533123', '500109', '411526', '532331', '370900', '450203',
        '320721', '451023', '542337', '331125', '441825', '451024', '370611', '420702', '211300', '331126', '610925',
        '220521', '511025', '512081', '530700', '341300', '371423', '632200', '441400', '340811', '640121', '350921',
        '430500', '150202', '522730', '371524', '360281', '632126', '120103', '431129', '360721', '230231', '230505',
        '150624', '620602', '140602', '150102', '131125', '530428', '610425', '431121', '340403', '360482', '652800',
        '430111', '540100', '513225', '230281', '210111', '530122', '320404', '510132', '621227', '511524', '530422',
        '371424', '623024', '350623', '140524', '330212', '632625', '500229', '361021', '431300', '371328', '360802',
        '330402', '513227', '140828', '231084', '370784', '421302', '360104', '510115', '431229', '441427', '130623',
        '532627', '141002', '430922', '320105', '420923', '320321', '522322', '150502', '130224', '370811', '510105',
        '450226', '430923', '450125', '220283', '361181', '310105', '371728', '450703', '230205', '210411', '350924',
        '431228', '530523', '620826', '210381', '513323', '350500', '130184', '150902', '341700', '530524', '341126',
        '542129', '210700', '232721', '370181', '321203', '411602', '542627', '330502', '330683', '510113', '141182',
        '360981', '350926', '360600', '430602', '141026', '320500', '542331', '640422', '610000', '230623', '422827',
        '632621', '610825', '640181', '530502', '370124', '610902', '350502', '230207', '360202', '650204', '140725',
        '420804', '445221', '370321', '230708', '360825', '430821', '511823', '220681', '150103', '410404', '530721',
        '440281', '530626', '659003', '652900', '341023', '510129', '340102', '420700', '410211', '140928', '511724',
        '610827', '410700', '500114', '632222', '330282', '330921', '130430', '610103', '511403', '152921', '371121',
        '441882', '370826', '451302', '361125', '610122', '230522', '510683', '130928', '520400', '533300', '350900',
        '532301', '210505', '411626', '532927', '150104', '522729', '451102', '542224', '340123', '610526', '610829',
        '141121', '430104', '440900', '140724', '542524', '360622', '130132', '510104', '610628', '330800', '500234',
        '340823', '220605', '210283', '230125', '220602', '511321', '522702', '370704', '341525', '410500', '130229',
        '230110', '130534', '653100', '320581', '530923', '530825', '152531', '513335', '410185', '360521', '120111',
        '341600', '350982', '230506', '370212', '350425', '360722', '610632', '320211', '370503', '450922', '230707',
        '542338', '320400', '422800', '211121', '469033', '610900', '530802', '513233', '141128', '530121', '230230',
        '411425', '340103', '140123', '211382', '440300', '371521', '542623', '370523', '810000', '210104', '632128',
        '340104', '530127', '500236', '620523', '450330', '350104', '140225', '542329', '210711', '411329', '429005',
        '441323', '620421', '542625', '310115', '469030', '152222', '370285', '330481', '421221', '533422', '150802',
        '140702', '513426', '440981', '230225', '510682', '420100', '232723', '231283', '522728', '130633', '140781',
        '450312', '510304', '370281', '350981', '451002', '621122', '350526', '350402', '341881', '371603', '411403',
        '371721', '620121', '450000', '140932', '430726', '310108', '360782', '340700', '530926', '622923', '610728',
        '140424', '510000', '130432', '340503', '510723', '130103', '350724', '230102', '341602', '340122', '533323',
        '130429', '330900', '450881', '410922', '632821', '410523', '220422', '620321', '522727', '130627', '640122',
        '320900', '140728', '411104', '140721', '632800', '361100', '533122', '450403', '431028', '441702', '542325',
        '340800', '511402', '320705', '420600', '320925', '140826', '450325', '530321', '511827', '542222', '433125',
        '350525', '450602', '533103', '131024', '610328', '510182', '532822', '230705', '520103', '632624', '410104',
        '440704', '621025', '370300', '320923', '131182', '232702', '361126', '450324', '341324', '371600', '420503',
        '440404', '610327', '510722', '341022', '620724', '410724', '430528', '230800', '654200', '542125', '341502',
        '511129', '422801', '370902', '320303', '430102', '220421', '350822', '310230', '150725', '445100', '230713',
        '513427', '650103', '510821', '140122', '431124', '420202', '533124', '230204', '420300', '433123', '110106',
        '530113', '410727', '130824', '140930', '370681', '350703', '511802', '542121', '411729', '511821', '130632',
        '370282', '632127', '331181', '430981', '110105', '361102', '610624', '510704', '522628', '130133', '451200',
        '360102', '513331', '500115', '140624', '410184', '220581', '150222', '210905', '430181', '220582', '532823',
        '371724', '632723', '350902', '542600', '532502', '360122', '530821', '340826', '130304', '370521', '310114',
        '230200', '430725', '131025', '640104', '520621', '371400', '310118', '522326', '530126', '360502', '411281',
        '510108', '445303', '371422', '640423', '141129', '232703', '421321', '410305', '420982', '220722', '421123',
        '431123', '211282', '350421', '330521', '350723', '140931', '610500', '451031', '350622', '610114', '220822',
        '230113', '150821', '371323', '371723', '520222', '210911', '231282', '433127', '511922', '410503', '430302',
        '510626', '211102', '320507', '220402', '211302', '441226', '511523', '441823', '130900', '540123', '610721',
        '230208', '620721', '410202', '140303', '140431', '542100', '350824', '360700', '620300', '331081', '520200',
        '140900', '451221', '623000', '450702', '130203', '131023', '232700', '520402', '620621', '361029', '542327',
        '310112', '350627', '520113', '431127', '210604', '621023', '341024', '440111', '150785', '231225', '140400',
        '370921', '511123', '440205', '513230', '321102', '542326', '450600', '440803', '469031', '130638', '231100',
        '210402', '370602', '431024', '330326', '441827', '520302', '120112', '360427', '130524', '320202', '360111',
        '152923', '411381', '511781', '420526', '370600', '350524', '360823', '610927', '429006', '610200', '320505',
        '510321', '530900', '341204', '350581', '411600', '450329', '410603', '341522', '370830', '370684', '510400',
        '360203', '430621', '210400', '430624', '340504', '410106', '411422', '520123', '533325', '152900', '220323',
        '370700', '500121', '420881', '130600', '430112', '410411', '110114', '341200', '522722', '440306', '120116',
        '150302', '500233', '371103', '211204', '420222', '370883', '542233', '622922', '632626', '431224', '422828',
        '211100', '441800', '430406', '630121', '450503', '130825', '630100', '440507', '532801', '220221', '430200',
        '350211', '370306', '532626', '431321', '431128', '610126', '430529', '230902', '610629', '542232', '640400',
        '469001', '230621', '140921', '341100', '431227', '130634', '140109', '130281', '445224', '511722', '131181',
        '341422', '370634', '330327', '511725', '130522', '511622', '150782', '441500', '500243', '341003', '411528',
        '441424', '610125', '150304', '440513', '330602', '371502', '321081', '230503', '360428', '520526', '370103',
        '230606', '513231', '430224', '530100', '341802', '623026', '232704', '441300', '411728', '451402', '131082',
        '361025', '141033', '410402', '371481', '620200', '430521', '130629', '542128', '230605', '431223', '500118',
        '610929', '371329', '360124', '532328', '421127', '211000', '530425', '371621', '441900', '530102', '522300',
        '410923', '430682', '110109', '140000', '360702', '230108', '330205', '420900', '441224', '542223', '512002',
        '450326', '510603', '511111', '350423', '210421', '520622', '630103', '420822', '469005', '610928', '130531',
        '522600', '430781', '440903', '430000', '411000', '542328', '430921', '520424', '120225', '421281', '340621',
        '430400', '522626', '632622', '211224', '469024', '530724', '500000', '451027', '420606', '430103', '210811',
        '411202', '421122', '520303', '533102', '410181', '140622', '320000', '654300', '421022', '469007', '141082',
        '321182', '542421', '410704', '611024', '530125', '130682', '542422', '542332', '350721', '450721', '130431',
        '542123', '513333', '211200', '140925', '330624', '511102', '371482', '610525', '610104', '230306', '130804',
        '513338', '120223', '350426', '310106', '430802', '230603', '341202', '230502', '140726', '220403', '510903',
        '430381', '431281', '520327', '632300', '350600', '130521', '522633', '610528', '513437', '411627', '441283',
        '430281', '440113', '340181', '610727', '652201', '610113', '441302', '621022', '140203', '210502', '222406',
        '610722', '542626', '350200', '513429', '511923', '220600', '230803', '360423', '530302', '610429', '522623',
        '360881', '360103', '451421', '533321', '621100', '410108', '370686', '532623', '130604', '520330', '220724',
        '230224', '530326', '410102', '360828', '471.55', '430421', '230833', '450223', '511303', '510500', '632600',
        '450225', '330300', '350300', '370832', '230921', '532922', '321183', '511100', '450923', '360827', '610331',
        '511623', '440402', '511124', '370812', '150581', '620900', '210122', '511903', '420302', '610723', '150423',
        '610831', '330183', '230600', '220105', '440203', '370202', '610204', '632324', '231182', '130723', '420200',
        '210202', '110115', '513334', '532300', '513424', '510181', '532322', '410526', '130731', '500102', '620123',
        '130926', '150124', '220802', '511529', '320100', '211281', '370911', '130300', '330902', '510124', '411081',
        '441523', '512021', '430423', '331122', '451228', '371200', '150500', '450102', '445381', '220881', '330281',
        '530902', '620981', '431026', '210321', '511325', '440700', '640105', '420117', '130530', '530325', '542423',
        '460200', '131081', '130183', '530722', '520524', '371327', '520626', '230227', '510402', '210211', '620525',
        '371312', '141122', '530124', '431122', '510322', '510600', '370683', '620822', '430800', '532926', '371403',
        '341124', '150521', '230126', '632224', '140821', '533421', '445281', '530128', '130500', '330122', '451400',
        '130527', '320506', '632322', '510623', '130683', '411622', '530922', '431221', '350527', '231102', '371622',
        '520321', '450331', '370923', '360781', '130121', '610626', '340711', '340321', '340827', '360728', '620622',
        '411725', '632823', '513232', '420303', '513325', '610326', '511921', '512022', '141125', '430225', '350521',
        '610100', '411722', '500101', '540102', '150206', '320703', '210300', '430700', '430681', '440515', '650105',
        '220400', '659004', '220106', '431322', '230406', '420106', '330421', '632221', '500242', '451202', '500231',
        '430405', '445302', '450900', '130624', '420902', '152224', '210112', '141034', '141025', '320282', '411303',
        '511424', '620982', '410225', '441625', '510311', '371722', '420821', '433100', '611002', '430105', '510800',
        '520525', '520628', '450803', '420984', '450521', '230702', '532529', '510900', '360829', '340405', '421023',
        '450405', '450512', '410327', '410900', '120115', '441225', '150824', '411322', '410329', '350681', '421100',
        '520323', '532500', '420582', '411327', '130730', '510303', '440224', '533423', '220281', '130128', '140700',
        '320621', '140106', '230421', '440881', '430611', '230405', '610523', '440105', '231000', '441202', '360403',
        '331000', '542228', '513324', '422826', '211021', '440512', '231221', '421083', '441623', '230703', '130982',
        '511528', '420625', '431081', '330881', '623021', '370481', '130681', '350400', '620722', '511527', '220382',
        '320903', '441423', '530300', '140425', '320684', '530823', '420583', '350429', '420527', '510811', '350625',
        '370104', '511825', '341524', '152527', '610304', '542330', '431126', '320124', '510107', '500110', '310116',
        '220523', '330483', '230624', '500107', '141126', '530826', '150429', '150625', '430723', '320405', '150424',
        '141123', '445322', '513332', '340822', '310110', '130503', '231181', '340208', '130481', '411002', '532525',
        '210204', '410781', '623027', '530103', '510503', '360426', '130434', '610802', '340111', '500228', '654000',
        '130684', '511112', '530129', '350624', '150100', '350302', '350722', '210181', '411723', '469023', '522701',
        '500120', '511503', '420607', '141032', '350503', '360900', '210726', '350303', '610627', '620422', '360822',
        '542122', '350923', '650202', '511521', '430503', '441324', '320811', '140223', '520121', '451226', '621123',
        '150925', '410611', '340207', '420502', '341302', '210113', '140430', '150826', '450100', '320322', '511126',
        '410328', '610600', '350821', '341225', '411221', '231081', '130822', '150721', '421126', '530424', '130533',
        '220181', '330100', '450924', '320623', '410205', '451028', '360481', '532323', '140723', '430424', '350781',
        '510681', '630000', '341521', '210114', '220621', '371522', '230402', '431103', '320924', '410728', '411326',
        '150627', '330225', '350205', '331102', '210521', '150922', '350000', '620105', '650102', '500117', '431003',
        '320116', '513228', '360902', '530181', '421000', '330329', '650109', '410122', '430407', '610522', '150825',
        '422822', '150724', '130733', '130107', '450303', '130102', '430522', '520114', '440183', '650205', '410902',
        '211221', '150523', '131121', '440114', '620524', '220202', '230704', '420529', '610926', '441402', '370403',
        '130109', '430600', '140421', '520422', '451100', '360200', '370112', '140411', '130528', '431200', '510403',
        '320509', '140428', '150421', '150924', '230128', '450109', '220104', '512000', '321002', '640106', '610322',
        '411302', '420113', '440303', '231224', '511602', '371526', '360723', '320706', '410311', '371083', '341621',
        '230709', '230903', '320106', '340203', '411724', '621027', '340600', '140322', '130925', '542301', '140500',
        '650000', '653000', '411103', '310000', '410322', '210804', '510114', '371425', '330200', '640303', '532524',
        '430408', '230706', '340100', '431002', '230221', '210702', '361024', '610830', '511011', '350702', '610404',
        '611023', '622900', '530925', '441481', '341702', '230104', '441602', '431225', '510904', '530381', '211005',
        '230521', '340402', '350213', '450481', '320803', '360983', '440703', '450305', '140521', '450621', '511700',
        '610111', '150422', '320113', '230811', '511822', '330482', '451422', '522635', '130603', '621221', '430100',
        '140426', '150722', '420602', '321302', '130323', '410303', '350602', '430724', '469021', '410103', '431302',
        '210105', '411500', '330922', '360602', '320281', '632321', '370211', '152525', '532530', '610324', '222424',
        '350504', '430481', '340521', '330109', '410423', '350628', '511500', '360121', '520111', '610303', '350182',
        '513425', '231003', '152530', '321023', '320722', '440100', '532324', '442000', '530522', '321181', '140722',
        '340828', '420205', '120114', '371300', '140825', '511302', '610724', '120000', '410203', '610630', '610481',
        '360726', '340602', '230000', '632100', '445321', '220100', '350125', '152221', '150600', '469028', '513326',
        '621225', '141127', '130208', '210403', '450200', '410825', '150430', '330802', '431381', '469025', '520100',
        '150784', '411681', '500111', '410300', '150602', '610921', '440825', '350700', '330726', '341125', '211103',
        '469002', '320311', '320724', '141028', '522622', '510727', '130126', '520523', '610700', '532327', '130529',
        '411481', '150404', '130706', '610826', '140108', '330127', '152202', '230700', '210881', '640202', '451029',
        '411402', '210522', '130428', '410302', '361129', '511002', '370702', '140502', '360302', '321311', '320612',
        '330382', '211002', '410804', '410325', '330411', '420683', '420581', '450302', '421181', '330723', '532625',
        '320125', '654202', '510923', '520527', '120113', '610400', '510724', '500112', '230805', '632521', '622924',
        '430722', '230127', '652101', '140600', '220200', '532501', '230828', '410381', '430903', '431102', '141023',
        '530500', '542522', '441802', '341500', '511502', '450124', '360730', '411503', '320382', '632722', '440116',
        '511600', '341722', '130729', '620922', '445103', '450423', '520602', '520502', '210123', '130100', '340421',
        '130110', '451321', '640425', '421087', '410703', '360733', '361000', '410421', '340502', '451225', '350783',
        '340304', '110102', '330185', '360421', '371626', '410200', '430223', '360321', '621202', '310113', '530822',
        '511000', '340703', '441322', '510100', '310120', '532325', '450981', '130227', '469026', '610329', '441203',
        '623023', '220623', '210212', '530927', '320981', '140727', '341825', '430511', '451300', '451121', '330822',
        '410100', '350825', '640200', '622901', '361028', '410782', '650104', '341823', '620521', '610323', '350427',
        '610222', '710001', '445122', '652222', '350305', '150622', '532923', '211381', '370829', '210921', '620800',
        '510421', '431025', '511304', '632724', '430527', '532924', '360824', '340802', '340124', '620824', '210106',
        '640302', '632522', '431100', '331003', '330304', '513229', '152201', '130502', '510121', '621102', '331123',
        '230881', '510302', '441426', '520324', '530000', '460100', '370406', '451324', '140802', '320305', '131100',
        '440233', '542231', '610923', '130602', '152529', '451424', '341623', '430482', '632001', '440882', '320300',
        '410481', '620400', '511133', '371428', '450108', '130435', '140100', '441284', '340400', '370500', '522325',
        '500232', '411424', '211223', '431027', '820000', '530630', '360425', '360924', '441723', '513400', '431222',
        '433124', '350181', '421102', '410527', '532901', '522732', '210200', '330328', '511028', '513431', '360500',
        '530324', '370105', '370802', '210904', '510802', '610403', '370827', '230303', '445202', '330825', '220183',
        '542426', '530702', '530624', '360982', '130726', '220721', '110113', '320723', '511113', '511902', '210000',
        '220000', '513434', '350922', '640521', '371700', '371525', '341282', '220800', '222401', '130984', '210124',
        '621024', '340200', '430203', '150205', '210682', '371623', '321101', '341503', '230524', '150923', '210304',
        '341182', '411325', '320831', '130622', '130721', '220524', '220211', '350481', '653200', '542221', '222405',
        '450821', '211481', '232701', '330106', '360830', '150403', '120105', '140621', '460108', '361023', '141181',
        '530323', '340202', '500116', '331127', '360735', '321283', '513329', '340000', '620702', '420103', '411300',
        '513300', '450902', '130205', '360424', '361026', '140423', '650203', '231202', '410506', '130732', '320585',
        '341622', '321012', '620725', '370831', '530423', '371602', '130621', '230781', '130427', '140121', '620522',
        '650100', '510183', '320611', '440883', '130728', '533100', '610203', '370785', '231281', '130930', '450332',
        '621002', '130424', '150626', '141031', '230202', '610726', '511024', '210303', '110108', '532932', '410502',
        '341821', '210504', '150928', '340121', '411423', '620923', '610582', '130202', '610821', '360826', '330503',
        '610922', '610824', '341221', '610502', '130523', '152526', '430426', '230206', '421081', '150402', '420107',
        '130207', '341002', '210802', '110117', '513322', '451425', '450321', '540121', '371082', '130923', '360821',
        '510521', '370102', '140923', '140929', '542624', '140429', '500104', '620823', '370125', '431230', '441502',
        '441622', '450328', '510131', '211404', '110112', '621124', '210882', '140105', '320700', '230404', '150926',
        '532329', '350424', '361002', '330702', '150700', '350121', '420682', '320200', '140427', '420111', '542521',
        '500235', '640324', '542500', '450202', '621121', '410711', '450222', '411121', '130324', '150223', '542526',
        '360800', '140311', '150623', '621026', '140924', '210602', '360323', '371322', '632701', '131000', '513330',
        '451025', '130724', '220102', '231121', '419001', '350102', '411321', '610822', '350100', '511181', '622927',
        '532326', '441521', '530322', '220122', '450221', '410822', '231222', '371427', '231025', '532531', '360729',
        '460107', '330203', '150125', '530924', '431000', '150000', '370786', '211003', '411527', '510726', '130903',
        '370705', '220182', '520425', '140525', '500237', '371727', '532931', '542334', '429021', '420104', '350629',
        '330784', '370687', '469027', '440112', '540122', '141124', '210903', '370725', '620403', '341822', '130426',
        '210302', '621222', '430811', '360100', '360734', '542425', '450804', '370200', '650200', '231083', '513327',
        '140981', '340881', '321202', '220284', '611026', '441881', '522632', '231123', '522624', '130321', '420321',
        '451222', '350206', '320111', '330103', '445200', '411025', '520522', '440514', '410926', '211321', '150723',
        '370800', '632825', '371725', '430581', '420703', '321111', '340500', '410324', '632826', '610428', '530828',
        '430221', '513430', '230710', '610115', '411324', '430300', '513337', '230305', '371100', '542124', '450421',
        '350800', '370612', '650107', '410223', '640323', '371625', '520322', '130421', '441700', '211081', '210624',
        '310109', '530111', '410821', '510422', '620104', '131128', '511681', '540125', '420324', '610202', '230712',
        '131028', '222426', '510700', '610112', '640424', '350782', '222403', '433122', '210803', '420500', '430204',
        '220103', '130425', '511900', '510822', '360402', '610924', '130637', '530521', '130181', '140402', '421182',
        '430202', '522630', '441421', '610725', '230711', '141130', '441721', '320104', '522723', '140110', '620122',
        '140902', '542225', '513328', '211322', '320324', '652122', '510921', '422823', '420323', '130927', '370613',
        '522726', '220702', '440229', '330600', '230203', '141029', '511425', '500241', '640502', '522323', '411502',
        '361022', '532621', '510524', '520623', '410105', '330621', '360123', '220502', '621200', '530600', '540124',
        '210102', '420505', '410928', '321112', '130230', '150400', '451123', '511400', '630104', '321200', '420102',
        '451122', '640300', '230103', '610302', '350304', '320582', '411523', '350583', '420802', '610800', '610422',
        '430121', '230183', '421200', '542430', '540000', '430124', '341824', '150123', '330903', '140823', '340604',
        '361130', '610621', '610823', '632525', '331124', '620100', '150727', '420381', '141024', '130630', '220303',
        '140222', '370502', '411100', '360921', '411524', '120110', '140202', '441303', '141081', '451423', '530112',
        '440784', '522629', '411624', '520600', '230715', '431021', '361030', '451229', '230124', '131002', '530427',
        '230500', '220882', '513428', '632524', '130631', '621125', '440811', '410811', '621224', '445102', '140830',
        '610602', '430623', '450224', '530421', '222402', '320312', '130929', '460106', '370685', '411726', '510525',
        '533400', '130628', '450103', '441600', '542324', '360732', '321284', '330681', '532523', '340825', '620623',
        '441781', '440232', '451021', '430211', '640522', '330108', '422802', '410482', '220203', '130526', '130111',
        '511702', '620102', '431023', '330102', '130802', '320302', '411700', '340222', '410726', '510502', '320922',
        '510922', '230622', '532925', '530629', '520625', '532928', '440785', '420528', '131122', '620821', '632500',
        '421124', '371426', '620700', '542322', '441826', '623001', '360400', '420281', '150621', '350403', '410721',
        '210681', '652123', '140824', '130225', '370782', '440705', '210282', '130803', '231024', '433101', '130924',
        '230304', '350111', '330322', '621223', '150524', '230400', '532527', '440115', '371002', '220282', '361127',
        '120101', '433126', '513222', '130423', '542126', '210727', '450502', '610623', '371311', '210423', '445300',
        '520112', '652100', '140302', '500240', '410522', '330522', '620502', '440605', '451281', '640205', '620111',
        '542525', '411623', '410725', '450700', '441223', '330381', '420525', '370703', '320802', '141021', '350802',
        '340603', '542229', '620902', '210281', '131124', '230129', '522627', '330824', '530628', '450122', '152500',
        '450126', '130722', '230381', '371102', '632726', '420921', '451030', '513433', '530625', '360923', '350626',
        '371202', '650121', '130105', '431022', '431202', '530824', '340404', '141100', '141000', '450327', '330682',
        '360724', '451000', '421125', '140522', '632323', '450304', '411102', '120102', '431226', '410400', '510725',
        '511824', '420115', '331021', '360731', '341103', '610430', '350582', '532900', '150822', '360222', '341424',
        '469003', '320481', '350823', '130827', '331024', '140829', '610124', '350103', '140927', '130104', '341004',
        '440305', '522700', '610622', '440802', '230523', '350428', '450802', '131102', '330783', '410222', '532800',
        '542424', '429004', '220204', '510184', '210703', '220302', '330781', '410182', '340803', '370405', '513226',
        '511621', '210224', '632801', '450323', '430900', '520300', '622926', '420504', '140212', '320921', '450500',
        '350505', '652200', '360725', '350122', '653125', '640100', '340223', '440500', '230109', '520102', '520381',
        '411082', '371500', '440000', '410425', '410602', '411323', '130826', '361122', '230604', '500103', '542127',
        '530829', '513436', '211400', '421202', '150823', '231005', '542400', '310104', '321322', '411222', '430626',
        '610524', '360681', '370400', '500106', '152922', '623022', '370881', '150929', '371726', '210323', '152200',
        '420105', '320482', '361123', '341203', '150425', '130636', '510823', '522636', '140300', '152223', '370522',
        '150207', '532622', '140800', '360926', '330105', '410622', '511703', '211303', '340302', '140603', '140882',
        '150900', '330500', '130532', '520122', '370203', '320205', '440800', '653226', '130581', '340824', '430523',
        '371203', '130525', '370682', '130129', '321282', '350603', '310101', '230822', '320381', '310117', '110229',
        '320206', '411224', '411628', '340522', '150726', '361121', '441624', '350128', '320681', '120104', '410183',
        '542133', '542200', '330523', '370283', '450123', '460105', '130130', '152501', '620000', '513221', '220112',
        '220723', '330324', '140481', '371324', '230123', '410823', '360313', '632122', '320412', '520624', '411328',
        '650106', '610730', '210781', '371702', '360322', '220322', '130626', '340221', '220700', '513200', '120106',
        '500230', '460000', '513223', '469006', '211402', '231226', '513432', '451481', '520328', '532503', '469022',
        '540126', '440604', '340322', '630102', '210500', '420116', '530402', '210800', '231223', '532532', '440902',
        '469029', '630105', '611021', '430721', '231004', '511300', '411521', '130204', '150300', '652700', '150200',
        '130725', '441621', '421002', '420114', '420981', '520382', '331082', '231124', '632623', '620600', '370783',
        '410702', '621126', '330110', '420624', '420506', '320204', '150203', '220300', '150921', '430902', '450204',
        '341226', '150781', '450603', '230722', '210902', '210100', '371523', '450921', '440983', '530602', '130403',
        '350881', '530627', '440403', '230714', '361027', '330727', '411024', '370213', '140211', '220622', '152524',
        '530623', '450422', '610828', '411421', '230904', '450205', '370113', '130402', '420684', '522631', '450107',
        '520325', '513321', '632725', '440104', '620723', '652223', '420626', '341181', '371321', '321084', '140321',
        '420800', '152522', '440606', '330400', '620500', '611022', '411400', '540127', '520500', '370126', '410306',
        '410221', '360925', '441422', '522328', '411727', '411525', '230826', '530426', '520521', '620103', '310107',
        '140226', '632523', '450722', '410883', '520000', '360430', '330283', '450400', '640221', '433130', '610729',
        '370724', '420325', '340323', '150981', '630123', '350123', '131127', '370323', '220381', '610631', '371081',
        '522601', '150526', '610521', '420112', '411122', '131022', '659001', '130800', '640500', '430382', '440307',
        '110101', '440823', '230321']

# 生成6-14位
date = []
start = '19000101'
end = time.strftime('%Y%m%d', time.localtime())
datestart = datetime.datetime.strptime(start, '%Y%m%d')
dateend = datetime.datetime.strptime(end, '%Y%m%d')
while datestart < dateend:
    datestart += datetime.timedelta(days=1)
    date.append(datestart.strftime('%Y%m%d'))
# print(date)

# 生成15-16位
list = []
for i in range(0, 100):
    b = '%02d' % i
    list.append(b)
# print(list)

# 生成17位性别码


sfz=input('输入身份证号：')
while not re.findall('^([0-9|\*]{0,17})([0-9]|X)$',sfz):
        sfz=input('重新输入身份证号：')
idcards = []


def zhengze(str, x, y, list):
    l1 = []
    str1 = str[x:y]
    str1 = str1.replace('*', '.')
    # print(str)
    for i in range(len(list)):
        try:
            sss = re.findall(str1, list[i])
            # print(sss[0])
            sfzs = str.replace(str[x:y], sss[0])
            # print(sfzs)
            l1.append(sfzs)
        except:
            pass
    return l1


if sfz[16] == '*':
    x = input('确定性别（1、男；2、女）：')
    while not re.findall('^[1-2]+$', x):
        x = input("数量只能为1或2,请重新输入:")
    if x == '1':
        gender = ['1', '3', '5', '7', '9']
    else:
        gender = ['0', '2', '4', '6', '8']
else:
    gender = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

sfz_areas = zhengze(sfz, 0, 6, area)
# print(sfz_areas)
# print(len(sfz_areas))
for sfz_area in sfz_areas:
    sfz_dates = zhengze(sfz_area, 6, 14, date)
    # print(sfz_dates)
    # print(len(sfz_dates))
    for sfz_date in sfz_dates:
        sfz_lists = zhengze(sfz_date, 14, 16, list)
        # print(sfz_lists)
        for sfz_list in sfz_lists:
            sfz_genders = zhengze(sfz_list, 16, 17, gender)
            # print(sfz_genders)
            for sfz_gender in sfz_genders:
                count = map(lambda x: int(x[0]) * x[1],
                            zip(sfz_gender, [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]))
                k = sum(count) % 11
                s = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2'][k]
                if sfz[-1] == s:
                    idcards.append(sfz_gender)
for idcard in idcards:
    print(idcard)
print(len(idcards))
