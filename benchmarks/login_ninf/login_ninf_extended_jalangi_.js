J$.iids = {"8":[13,5,13,16],"9":[1,10,1,17],"10":[29,5,29,34],"16":[31,7,31,14],"17":[1,18,1,22],"18":[31,7,31,14],"24":[37,7,37,14],"25":[1,10,1,23],"26":[37,7,37,14],"32":[29,5,29,34],"33":[1,10,1,23],"34":[44,14,44,50],"41":[1,10,1,23],"49":[5,23,5,25],"57":[5,33,5,50],"65":[5,52,5,81],"73":[5,23,5,82],"75":[5,23,5,32],"81":[5,23,5,82],"89":[5,23,5,82],"97":[6,23,6,25],"105":[6,33,6,50],"113":[6,52,6,62],"121":[6,23,6,63],"123":[6,23,6,32],"129":[6,23,6,63],"137":[6,23,6,63],"145":[8,14,8,16],"153":[8,24,8,32],"161":[8,34,8,38],"169":[8,14,8,39],"171":[8,14,8,23],"177":[8,14,8,39],"185":[8,14,8,39],"193":[9,19,9,21],"201":[9,29,9,42],"209":[9,44,9,48],"217":[9,19,9,49],"219":[9,19,9,28],"225":[9,19,9,49],"233":[9,19,9,49],"241":[13,5,13,16],"249":[15,21,15,34],"257":[15,21,15,34],"265":[15,3,15,35],"273":[19,6,19,14],"281":[19,6,19,14],"289":[19,1,19,15],"297":[29,5,29,20],"305":[29,24,29,34],"313":[30,18,30,47],"321":[30,18,30,58],"323":[30,18,30,56],"329":[30,18,30,58],"337":[30,18,30,58],"345":[31,8,31,14],"353":[32,23,32,52],"361":[32,23,32,52],"369":[32,5,32,53],"377":[36,18,36,40],"385":[36,18,36,51],"387":[36,18,36,49],"393":[36,18,36,51],"401":[36,18,36,51],"409":[37,8,37,14],"417":[38,23,38,45],"425":[38,23,38,45],"433":[38,5,38,46],"441":[44,14,44,42],"449":[44,45,44,50],"457":[44,14,44,50],"465":[44,14,44,50],"473":[45,1,45,7],"481":[45,8,45,12],"489":[45,1,45,13],"497":[45,1,45,14],"505":[1,1,48,20],"513":[1,1,48,20],"521":[1,1,48,20],"529":[1,1,48,20],"537":[1,1,48,20],"545":[1,1,48,20],"553":[1,1,48,20],"561":[1,1,48,20],"569":[1,1,48,20],"577":[1,1,48,20],"585":[13,1,16,2],"593":[31,3,33,4],"601":[37,3,39,4],"609":[29,1,40,2],"617":[1,1,48,20],"625":[1,1,48,20],"nBranches":8,"originalCodeFileName":"/Users/tzuhan/+research/hyper_enforce/HyperEnforce/csf23_benchmarks/login_ninf/login_ninf_extended.js","instrumentedCodeFileName":"/Users/tzuhan/+research/hyper_enforce/HyperEnforce/csf23_benchmarks/login_ninf/login_ninf_extended_jalangi_.js","code":"var S$ = require('S$');\n// var longitude = 0;\n// var latitude = 0;\n/* SYMBOLIC VARS */\nvar con_str_baseUrl = S$.symbol('con_str_baseUrl', 'mysite.com/intern/login.php');\nvar ucon_str_cookie = S$.symbol('ucon_str_cookie', 'isIntern');\n// var ucon_user = S$.symbol('ucon_user', 'null');\nvar supp_0 = S$.symbol('supp_0', true)\nvar ucon_select = S$.symbol('ucon_select', true)\n\n// S$.assume(((ucon_str_cooki == \"isIntern\") || (con_str_baseUrl == \"isNotIntern\")))\n// if ((con_str_baseUrl == \"mysite.com/login.php\")) { }\nif (ucon_select){\n//     con_str_baseUrl = 'mysite.com/login.php'\n    ucon_str_cookie = 'isNotIntern'\n}\nvar id\n// var src\nid  = 'AdNode'\n// src = 'adserver.com/display.js'\n\n// var ucon_user = document.getElementById(\"User\").text;\n\n\n/* MAIN JS PROGRAM */\n// var baseUrl;\n\n// var settings = function(s) { baseUrl = s; }\nif(ucon_str_cookie == (\"isIntern\")) {\n  var aux_add1 = \"mysite.com/intern/login.php\".toString()\n  if(!supp_0){\n  con_str_baseUrl = 'mysite.com/intern/login.php'\n  }\n}\nelse {\n  var aux_add2 = \"mysite.com/login.php\".toString()\n  if(!supp_0){\n  con_str_baseUrl = 'mysite.com/login.php'\n  }\n}\n\n\n// text += document.getElementById(\"Pwd\").text;\nvar imgSrc = \"http://example.com/img.jpg\"+ \"?t=\"\nescape(text);\n// document.getElementById(\"img\").src = imgSrc;\n\n/// END OF FILE ///\n"};
jalangiLabel0:
    while (true) {
        try {
            J$.Se(505, '/Users/tzuhan/+research/hyper_enforce/HyperEnforce/csf23_benchmarks/login_ninf/login_ninf_extended_jalangi_.js', '/Users/tzuhan/+research/hyper_enforce/HyperEnforce/csf23_benchmarks/login_ninf/login_ninf_extended.js');
            J$.N(513, 'S$', S$, 0);
            J$.N(521, 'con_str_baseUrl', con_str_baseUrl, 0);
            J$.N(529, 'ucon_str_cookie', ucon_str_cookie, 0);
            J$.N(537, 'supp_0', supp_0, 0);
            J$.N(545, 'ucon_select', ucon_select, 0);
            J$.N(553, 'id', id, 0);
            J$.N(561, 'aux_add1', aux_add1, 0);
            J$.N(569, 'aux_add2', aux_add2, 0);
            J$.N(577, 'imgSrc', imgSrc, 0);
            var S$ = J$.X1(41, J$.W(33, 'S$', J$.F(25, J$.R(9, 'require', require, 2), 0)(J$.T(17, 'S$', 21, false)), S$, 3));
            var con_str_baseUrl = J$.X1(89, J$.W(81, 'con_str_baseUrl', J$.M(73, J$.R(49, 'S$', S$, 1), 'symbol', 0)(J$.T(57, 'con_str_baseUrl', 21, false), J$.T(65, 'mysite.com/intern/login.php', 21, false)), con_str_baseUrl, 3));
            var ucon_str_cookie = J$.X1(137, J$.W(129, 'ucon_str_cookie', J$.M(121, J$.R(97, 'S$', S$, 1), 'symbol', 0)(J$.T(105, 'ucon_str_cookie', 21, false), J$.T(113, 'isIntern', 21, false)), ucon_str_cookie, 3));
            var supp_0 = J$.X1(185, J$.W(177, 'supp_0', J$.M(169, J$.R(145, 'S$', S$, 1), 'symbol', 0)(J$.T(153, 'supp_0', 21, false), J$.T(161, true, 23, false)), supp_0, 3));
            var ucon_select = J$.X1(233, J$.W(225, 'ucon_select', J$.M(217, J$.R(193, 'S$', S$, 1), 'symbol', 0)(J$.T(201, 'ucon_select', 21, false), J$.T(209, true, 23, false)), ucon_select, 3));
            if (J$.X1(585, J$.C(8, J$.R(241, 'ucon_select', ucon_select, 1)))) {
                J$.X1(265, ucon_str_cookie = J$.W(257, 'ucon_str_cookie', J$.T(249, 'isNotIntern', 21, false), ucon_str_cookie, 2));
            }
            var id;
            J$.X1(289, id = J$.W(281, 'id', J$.T(273, 'AdNode', 21, false), id, 2));
            if (J$.X1(609, J$.C(32, J$.B(10, '==', J$.R(297, 'ucon_str_cookie', ucon_str_cookie, 1), J$.T(305, "isIntern", 21, false), 0)))) {
                var aux_add1 = J$.X1(337, J$.W(329, 'aux_add1', J$.M(321, J$.T(313, "mysite.com/intern/login.php", 21, false), 'toString', 0)(), aux_add1, 3));
                if (J$.X1(593, J$.C(16, J$.U(18, '!', J$.R(345, 'supp_0', supp_0, 1))))) {
                    J$.X1(369, con_str_baseUrl = J$.W(361, 'con_str_baseUrl', J$.T(353, 'mysite.com/intern/login.php', 21, false), con_str_baseUrl, 2));
                }
            } else {
                var aux_add2 = J$.X1(401, J$.W(393, 'aux_add2', J$.M(385, J$.T(377, "mysite.com/login.php", 21, false), 'toString', 0)(), aux_add2, 3));
                if (J$.X1(601, J$.C(24, J$.U(26, '!', J$.R(409, 'supp_0', supp_0, 1))))) {
                    J$.X1(433, con_str_baseUrl = J$.W(425, 'con_str_baseUrl', J$.T(417, 'mysite.com/login.php', 21, false), con_str_baseUrl, 2));
                }
            }
            var imgSrc = J$.X1(465, J$.W(457, 'imgSrc', J$.B(34, '+', J$.T(441, "http://example.com/img.jpg", 21, false), J$.T(449, "?t=", 21, false), 0), imgSrc, 3));
            J$.X1(497, J$.F(489, J$.R(473, 'escape', escape, 2), 0)(J$.R(481, 'text', text, 2)));
        } catch (J$e) {
            J$.Ex(617, J$e);
        } finally {
            if (J$.Sr(625)) {
                J$.L();
                continue jalangiLabel0;
            } else {
                J$.L();
                break jalangiLabel0;
            }
        }
    }
// JALANGI DO NOT INSTRUMENT
