J$.iids = {"8":[42,5,42,30],"9":[1,10,1,17],"10":[42,5,42,30],"17":[1,18,1,22],"25":[1,10,1,23],"33":[1,10,1,23],"41":[1,10,1,23],"49":[5,19,5,21],"57":[5,29,5,42],"65":[5,44,5,50],"73":[5,19,5,51],"75":[5,19,5,28],"81":[5,19,5,51],"89":[5,19,5,51],"97":[6,19,6,21],"105":[6,29,6,42],"113":[6,44,6,50],"121":[6,19,6,51],"123":[6,19,6,28],"129":[6,19,6,51],"137":[6,19,6,51],"145":[42,5,42,16],"153":[42,20,42,30],"161":[44,17,44,46],"169":[44,17,44,46],"177":[44,3,44,47],"185":[48,17,48,39],"193":[48,17,48,39],"201":[48,3,48,40],"209":[55,6,55,14],"217":[55,6,55,14],"225":[55,1,55,15],"233":[56,7,56,32],"241":[56,7,56,32],"249":[56,1,56,33],"257":[1,1,58,20],"265":[1,1,58,20],"273":[1,1,58,20],"281":[1,1,58,20],"289":[1,1,58,20],"297":[1,1,58,20],"305":[42,1,50,2],"313":[1,1,58,20],"321":[1,1,58,20],"nBranches":2,"originalCodeFileName":"/Users/tzuhan/+research/hyper_enforce/HyperEnforce/csf23_benchmarks/login/login_extended.js","instrumentedCodeFileName":"/Users/tzuhan/+research/hyper_enforce/HyperEnforce/csf23_benchmarks/login/login_extended_jalangi_.js","code":"var S$ = require('S$');\n// var longitude = 0;\n// var latitude = 0;\n/* SYMBOLIC VARS */\nvar con_baseUrl = S$.symbol('con_baseUrl', 'null');\nvar ucon_cookie = S$.symbol('ucon_cookie', 'null');\n// var supp_0 = S$.symbol('supp_0', true)\n// var supp_1 = S$.symbol('supp_1', true)\n\n// var random_num = \"\"\n// function getRandomNum(){\n//   num = Math.floor(Math.random() * (10 - 0) + 0)\n//   random_num = str(num)\n// }\n// getRandomNum()\n// (con_longitude == random_num)\n// if((con_latitude == '10')){\n  // if((con_longitude == '10')){\n  // }\n// }\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n  // }\n// }\n/* MAIN JS PROGRAM */\n// var baseUrl;\n\n// var settings = function(s) { baseUrl = s; }\n\nif(ucon_cookie == (\"isIntern\")) {\n  // var aux_add = 'mysite.com/intern/login.php'\n  con_baseUrl = 'mysite.com/intern/login.php'\n\n} else {\n  // var aux_add = 'mysite.com/login.php'\n  con_baseUrl = 'mysite.com/login.php'\n// settings(\"mysite.com/login.php\");\n}\n\nvar id\nvar src\n\nid = 'AdNode'\nsrc= 'adserver.com/display.js'\n\n/// END OF FILE ///\n"};
jalangiLabel0:
    while (true) {
        try {
            J$.Se(257, '/Users/tzuhan/+research/hyper_enforce/HyperEnforce/csf23_benchmarks/login/login_extended_jalangi_.js', '/Users/tzuhan/+research/hyper_enforce/HyperEnforce/csf23_benchmarks/login/login_extended.js');
            J$.N(265, 'S$', S$, 0);
            J$.N(273, 'con_baseUrl', con_baseUrl, 0);
            J$.N(281, 'ucon_cookie', ucon_cookie, 0);
            J$.N(289, 'id', id, 0);
            J$.N(297, 'src', src, 0);
            var S$ = J$.X1(41, J$.W(33, 'S$', J$.F(25, J$.R(9, 'require', require, 2), 0)(J$.T(17, 'S$', 21, false)), S$, 3));
            var con_baseUrl = J$.X1(89, J$.W(81, 'con_baseUrl', J$.M(73, J$.R(49, 'S$', S$, 1), 'symbol', 0)(J$.T(57, 'con_baseUrl', 21, false), J$.T(65, 'null', 21, false)), con_baseUrl, 3));
            var ucon_cookie = J$.X1(137, J$.W(129, 'ucon_cookie', J$.M(121, J$.R(97, 'S$', S$, 1), 'symbol', 0)(J$.T(105, 'ucon_cookie', 21, false), J$.T(113, 'null', 21, false)), ucon_cookie, 3));
            if (J$.X1(305, J$.C(8, J$.B(10, '==', J$.R(145, 'ucon_cookie', ucon_cookie, 1), J$.T(153, "isIntern", 21, false), 0)))) {
                J$.X1(177, con_baseUrl = J$.W(169, 'con_baseUrl', J$.T(161, 'mysite.com/intern/login.php', 21, false), con_baseUrl, 2));
            } else {
                J$.X1(201, con_baseUrl = J$.W(193, 'con_baseUrl', J$.T(185, 'mysite.com/login.php', 21, false), con_baseUrl, 2));
            }
            var id;
            var src;
            J$.X1(225, id = J$.W(217, 'id', J$.T(209, 'AdNode', 21, false), id, 2));
            J$.X1(249, src = J$.W(241, 'src', J$.T(233, 'adserver.com/display.js', 21, false), src, 2));
        } catch (J$e) {
            J$.Ex(313, J$e);
        } finally {
            if (J$.Sr(321)) {
                J$.L();
                continue jalangiLabel0;
            } else {
                J$.L();
                break jalangiLabel0;
            }
        }
    }
// JALANGI DO NOT INSTRUMENT
