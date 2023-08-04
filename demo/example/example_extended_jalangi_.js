J$.iids = {"8":[12,5,12,11],"9":[1,10,1,17],"10":[19,7,19,14],"16":[19,7,19,14],"17":[1,18,1,22],"24":[18,5,18,11],"25":[1,10,1,23],"33":[1,10,1,23],"41":[1,10,1,23],"49":[4,14,4,16],"57":[4,24,4,32],"65":[4,34,4,38],"73":[4,14,4,39],"75":[4,14,4,23],"81":[4,14,4,39],"89":[4,14,4,39],"97":[5,14,5,16],"105":[5,24,5,32],"113":[5,34,5,38],"121":[5,14,5,39],"123":[5,14,5,23],"129":[5,14,5,39],"137":[5,14,5,39],"145":[6,13,6,15],"153":[6,23,6,30],"161":[6,32,6,36],"169":[6,13,6,37],"171":[6,13,6,22],"177":[6,13,6,37],"185":[6,13,6,37],"193":[7,14,7,16],"201":[7,24,7,32],"209":[7,34,7,38],"217":[7,14,7,39],"219":[7,14,7,23],"225":[7,14,7,39],"233":[7,14,7,39],"241":[12,5,12,11],"249":[13,12,13,16],"257":[13,12,13,16],"265":[13,3,13,17],"273":[16,12,16,17],"281":[16,12,16,17],"289":[16,3,16,18],"297":[18,5,18,11],"305":[19,8,19,14],"313":[20,13,20,18],"321":[20,13,20,18],"329":[20,5,20,19],"337":[1,1,27,27],"345":[1,1,27,27],"353":[1,1,27,27],"361":[1,1,27,27],"369":[1,1,27,27],"377":[1,1,27,27],"385":[12,1,17,2],"393":[19,3,21,4],"401":[18,1,22,2],"409":[1,1,27,27],"417":[1,1,27,27],"nBranches":6,"originalCodeFileName":"/Users/tzuhan/+research/hyper_enforce/HyperEnforce/demo/example/example_extended.js","instrumentedCodeFileName":"/Users/tzuhan/+research/hyper_enforce/HyperEnforce/demo/example/example_extended_jalangi_.js","code":"var S$ = require('S$');\n\n/* SYMBOLIC VARS */\nvar ucon_x = S$.symbol('ucon_x', true);\nvar ucon_z = S$.symbol('ucon_z', true);\nvar con_y = S$.symbol('con_y', true);\nvar supp_0 = S$.symbol('supp_0', true)\n\n\n\n/* MAIN JS PROGRAM */\nif(ucon_z){\n  ucon_x = true\n}\nelse{\n  ucon_x = false\n}\nif (ucon_x){\n  if (!supp_0){\n    con_y = false\n  }\n}\n/* END OF FILE */\n\n// if (ucon_x == false) {}\n// if (con_y == false) {}\n// if (ucon_z == false) {}\n"};
jalangiLabel0:
    while (true) {
        try {
            J$.Se(337, '/Users/tzuhan/+research/hyper_enforce/HyperEnforce/demo/example/example_extended_jalangi_.js', '/Users/tzuhan/+research/hyper_enforce/HyperEnforce/demo/example/example_extended.js');
            J$.N(345, 'S$', S$, 0);
            J$.N(353, 'ucon_x', ucon_x, 0);
            J$.N(361, 'ucon_z', ucon_z, 0);
            J$.N(369, 'con_y', con_y, 0);
            J$.N(377, 'supp_0', supp_0, 0);
            var S$ = J$.X1(41, J$.W(33, 'S$', J$.F(25, J$.R(9, 'require', require, 2), 0)(J$.T(17, 'S$', 21, false)), S$, 3));
            var ucon_x = J$.X1(89, J$.W(81, 'ucon_x', J$.M(73, J$.R(49, 'S$', S$, 1), 'symbol', 0)(J$.T(57, 'ucon_x', 21, false), J$.T(65, true, 23, false)), ucon_x, 3));
            var ucon_z = J$.X1(137, J$.W(129, 'ucon_z', J$.M(121, J$.R(97, 'S$', S$, 1), 'symbol', 0)(J$.T(105, 'ucon_z', 21, false), J$.T(113, true, 23, false)), ucon_z, 3));
            var con_y = J$.X1(185, J$.W(177, 'con_y', J$.M(169, J$.R(145, 'S$', S$, 1), 'symbol', 0)(J$.T(153, 'con_y', 21, false), J$.T(161, true, 23, false)), con_y, 3));
            var supp_0 = J$.X1(233, J$.W(225, 'supp_0', J$.M(217, J$.R(193, 'S$', S$, 1), 'symbol', 0)(J$.T(201, 'supp_0', 21, false), J$.T(209, true, 23, false)), supp_0, 3));
            if (J$.X1(385, J$.C(8, J$.R(241, 'ucon_z', ucon_z, 1)))) {
                J$.X1(265, ucon_x = J$.W(257, 'ucon_x', J$.T(249, true, 23, false), ucon_x, 2));
            } else {
                J$.X1(289, ucon_x = J$.W(281, 'ucon_x', J$.T(273, false, 23, false), ucon_x, 2));
            }
            if (J$.X1(401, J$.C(24, J$.R(297, 'ucon_x', ucon_x, 1)))) {
                if (J$.X1(393, J$.C(16, J$.U(10, '!', J$.R(305, 'supp_0', supp_0, 1))))) {
                    J$.X1(329, con_y = J$.W(321, 'con_y', J$.T(313, false, 23, false), con_y, 2));
                }
            }
        } catch (J$e) {
            J$.Ex(409, J$e);
        } finally {
            if (J$.Sr(417)) {
                J$.L();
                continue jalangiLabel0;
            } else {
                J$.L();
                break jalangiLabel0;
            }
        }
    }
// JALANGI DO NOT INSTRUMENT
