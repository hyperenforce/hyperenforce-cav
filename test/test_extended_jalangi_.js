J$.iids = {"8":[29,7,29,18],"9":[1,10,1,17],"16":[28,5,28,11],"17":[1,18,1,22],"25":[1,10,1,23],"33":[1,10,1,23],"41":[1,10,1,23],"49":[9,19,9,21],"57":[9,29,9,42],"65":[9,44,9,48],"73":[9,19,9,49],"75":[9,19,9,28],"81":[9,19,9,49],"89":[9,19,9,49],"97":[12,14,12,16],"105":[12,24,12,32],"113":[12,34,12,38],"121":[12,14,12,39],"123":[12,14,12,23],"129":[12,14,12,39],"137":[12,14,12,39],"145":[15,13,15,15],"153":[15,23,15,30],"161":[15,32,15,36],"169":[15,13,15,37],"171":[15,13,15,22],"177":[15,13,15,37],"185":[15,13,15,37],"193":[28,5,28,11],"201":[29,7,29,18],"209":[30,13,30,18],"217":[30,13,30,18],"225":[30,5,30,19],"233":[1,1,34,20],"241":[1,1,34,20],"249":[1,1,34,20],"257":[1,1,34,20],"265":[1,1,34,20],"273":[29,3,32,4],"281":[28,1,33,2],"289":[1,1,34,20],"297":[1,1,34,20],"nBranches":4,"originalCodeFileName":"/Users/tzuhan/+research/hyper_enforce/HyperEnforce/test/test_extended.js","instrumentedCodeFileName":"/Users/tzuhan/+research/hyper_enforce/HyperEnforce/test/test_extended_jalangi_.js","code":"var S$ = require('S$');\r\n\r\n// var con_ucon_x_0 = S$.symbol('con_ucon_x_0',true);\r\n\r\n\r\n// var con_con_y_1 = S$.symbol('con_con_y_1',true);\r\n\r\n\r\nvar con_con_y_2 = S$.symbol('con_con_y_2',true);\r\n\r\n\r\nvar ucon_x = S$.symbol('ucon_x',true);\r\n\r\n\r\nvar con_y = S$.symbol('con_y',true);\r\n\r\n\r\n/* VARS */\r\n// if (con_ucon_x_0){\r\n//  ucon_x  = (Math.random() < 0.5)\r\n\r\n// }\r\n// if (con_con_y_1){\r\n//  con_y   = (Math.random() < 0.5)\r\n\r\n// }\r\n/* MAIN JS PROGRAM */\r\nif (ucon_x){\r\n  if (con_con_y_2){\r\n   con_y = false\r\n\r\n  }\r\n}\r\n/// END OF FILE ///\r\n"};
jalangiLabel0:
    while (true) {
        try {
            J$.Se(233, '/Users/tzuhan/+research/hyper_enforce/HyperEnforce/test/test_extended_jalangi_.js', '/Users/tzuhan/+research/hyper_enforce/HyperEnforce/test/test_extended.js');
            J$.N(241, 'S$', S$, 0);
            J$.N(249, 'con_con_y_2', con_con_y_2, 0);
            J$.N(257, 'ucon_x', ucon_x, 0);
            J$.N(265, 'con_y', con_y, 0);
            var S$ = J$.X1(41, J$.W(33, 'S$', J$.F(25, J$.R(9, 'require', require, 2), 0)(J$.T(17, 'S$', 21, false)), S$, 3));
            var con_con_y_2 = J$.X1(89, J$.W(81, 'con_con_y_2', J$.M(73, J$.R(49, 'S$', S$, 1), 'symbol', 0)(J$.T(57, 'con_con_y_2', 21, false), J$.T(65, true, 23, false)), con_con_y_2, 3));
            var ucon_x = J$.X1(137, J$.W(129, 'ucon_x', J$.M(121, J$.R(97, 'S$', S$, 1), 'symbol', 0)(J$.T(105, 'ucon_x', 21, false), J$.T(113, true, 23, false)), ucon_x, 3));
            var con_y = J$.X1(185, J$.W(177, 'con_y', J$.M(169, J$.R(145, 'S$', S$, 1), 'symbol', 0)(J$.T(153, 'con_y', 21, false), J$.T(161, true, 23, false)), con_y, 3));
            if (J$.X1(281, J$.C(16, J$.R(193, 'ucon_x', ucon_x, 1)))) {
                if (J$.X1(273, J$.C(8, J$.R(201, 'con_con_y_2', con_con_y_2, 1)))) {
                    J$.X1(225, con_y = J$.W(217, 'con_y', J$.T(209, false, 23, false), con_y, 2));
                }
            }
        } catch (J$e) {
            J$.Ex(289, J$e);
        } finally {
            if (J$.Sr(297)) {
                J$.L();
                continue jalangiLabel0;
            } else {
                J$.L();
                break jalangiLabel0;
            }
        }
    }
// JALANGI DO NOT INSTRUMENT
