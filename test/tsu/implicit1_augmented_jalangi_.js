J$.iids = {"8":[17,7,17,18],"9":[1,10,1,17],"16":[16,5,16,11],"17":[1,18,1,22],"25":[1,10,1,23],"33":[1,10,1,23],"41":[1,10,1,23],"49":[3,19,3,21],"57":[3,29,3,42],"65":[3,44,3,48],"73":[3,19,3,49],"75":[3,19,3,28],"81":[3,19,3,49],"89":[3,19,3,49],"97":[6,14,6,16],"105":[6,24,6,32],"113":[6,34,6,35],"121":[6,14,6,36],"123":[6,14,6,23],"129":[6,14,6,36],"137":[6,14,6,36],"145":[9,13,9,15],"153":[9,23,9,30],"161":[9,32,9,33],"169":[9,13,9,34],"171":[9,13,9,22],"177":[9,13,9,34],"185":[9,13,9,34],"193":[16,5,16,11],"201":[17,7,17,18],"209":[18,13,18,18],"217":[18,13,18,18],"225":[18,5,18,19],"233":[1,1,22,20],"241":[1,1,22,20],"249":[1,1,22,20],"257":[1,1,22,20],"265":[1,1,22,20],"273":[17,3,20,4],"281":[16,1,21,2],"289":[1,1,22,20],"297":[1,1,22,20],"nBranches":4,"originalCodeFileName":"/Users/tzuhan/+research/hyper_enforce/HyperEnforce/test/tsu/implicit1_augmented.js","instrumentedCodeFileName":"/Users/tzuhan/+research/hyper_enforce/HyperEnforce/test/tsu/implicit1_augmented_jalangi_.js","code":"var S$ = require('S$');\r\n\r\nvar con_con_y_0 = S$.symbol('con_con_y_0',true);\r\n\r\n\r\nvar ucon_x = S$.symbol('ucon_x',0);\r\n\r\n\r\nvar con_y = S$.symbol('con_y',0);\r\n\r\n\r\n/* VARS */\r\n// ucon_x  = (Math.random() < 0.5)\r\n// con_y   = (Math.random() < 0.5)\r\n/* MAIN JS PROGRAM */\r\nif (ucon_x){\r\n  if (con_con_y_0){ \r\n   con_y = false\r\n \r\n  }\r\n}\r\n/// END OF FILE ///\r\n"};
jalangiLabel0:
    while (true) {
        try {
            J$.Se(233, '/Users/tzuhan/+research/hyper_enforce/HyperEnforce/test/tsu/implicit1_augmented_jalangi_.js', '/Users/tzuhan/+research/hyper_enforce/HyperEnforce/test/tsu/implicit1_augmented.js');
            J$.N(241, 'S$', S$, 0);
            J$.N(249, 'con_con_y_0', con_con_y_0, 0);
            J$.N(257, 'ucon_x', ucon_x, 0);
            J$.N(265, 'con_y', con_y, 0);
            var S$ = J$.X1(41, J$.W(33, 'S$', J$.F(25, J$.R(9, 'require', require, 2), 0)(J$.T(17, 'S$', 21, false)), S$, 3));
            var con_con_y_0 = J$.X1(89, J$.W(81, 'con_con_y_0', J$.M(73, J$.R(49, 'S$', S$, 1), 'symbol', 0)(J$.T(57, 'con_con_y_0', 21, false), J$.T(65, true, 23, false)), con_con_y_0, 3));
            var ucon_x = J$.X1(137, J$.W(129, 'ucon_x', J$.M(121, J$.R(97, 'S$', S$, 1), 'symbol', 0)(J$.T(105, 'ucon_x', 21, false), J$.T(113, 0, 22, false)), ucon_x, 3));
            var con_y = J$.X1(185, J$.W(177, 'con_y', J$.M(169, J$.R(145, 'S$', S$, 1), 'symbol', 0)(J$.T(153, 'con_y', 21, false), J$.T(161, 0, 22, false)), con_y, 3));
            if (J$.X1(281, J$.C(16, J$.R(193, 'ucon_x', ucon_x, 1)))) {
                if (J$.X1(273, J$.C(8, J$.R(201, 'con_con_y_0', con_con_y_0, 1)))) {
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
