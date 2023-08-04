J$.iids = {"8":[29,4,29,10],"9":[9,10,9,14],"16":[40,4,40,10],"17":[9,10,9,14],"25":[9,1,9,15],"33":[9,25,9,29],"41":[9,25,9,29],"49":[9,16,9,30],"57":[9,39,9,43],"65":[9,39,9,43],"73":[9,31,9,44],"81":[15,3,15,10],"89":[15,15,15,42],"97":[15,3,15,43],"99":[15,3,15,14],"105":[15,3,15,43],"113":[14,10,16,2],"121":[14,10,16,2],"129":[14,10,16,2],"137":[14,10,16,2],"145":[14,10,16,2],"153":[14,10,16,2],"161":[14,10,16,2],"169":[14,1,16,2],"177":[17,15,19,2],"185":[17,15,19,2],"193":[17,15,19,2],"201":[17,15,19,2],"209":[17,15,19,2],"217":[17,15,19,2],"225":[17,15,19,2],"233":[17,1,19,2],"241":[23,1,23,8],"249":[23,13,23,33],"257":[23,1,23,34],"259":[23,1,23,12],"265":[23,1,23,34],"273":[24,1,24,8],"281":[24,13,24,37],"289":[24,1,24,38],"291":[24,1,24,12],"297":[24,1,24,38],"305":[25,1,25,8],"313":[25,13,25,24],"321":[25,25,25,31],"329":[25,33,25,39],"337":[25,41,25,46],"345":[25,13,25,47],"353":[25,1,25,48],"355":[25,1,25,12],"361":[25,1,25,48],"369":[27,1,27,8],"377":[27,13,27,33],"385":[27,1,27,34],"387":[27,1,27,12],"393":[27,1,27,34],"401":[28,1,28,8],"409":[28,13,28,43],"417":[28,1,28,44],"419":[28,1,28,12],"425":[28,1,28,44],"433":[29,4,29,10],"441":[30,12,30,16],"449":[30,12,30,16],"457":[30,3,30,16],"465":[33,12,33,17],"473":[33,12,33,17],"481":[33,3,33,17],"489":[35,1,35,8],"497":[35,13,35,24],"505":[35,25,35,31],"513":[35,33,35,39],"521":[35,41,35,46],"529":[35,13,35,47],"537":[35,1,35,48],"539":[35,1,35,12],"545":[35,1,35,48],"553":[37,1,37,8],"561":[37,13,37,33],"569":[37,1,37,34],"571":[37,1,37,12],"577":[37,1,37,34],"585":[38,1,38,8],"593":[38,13,38,44],"601":[38,1,38,45],"603":[38,1,38,12],"609":[38,1,38,45],"617":[40,4,40,10],"625":[41,11,41,17],"633":[41,18,41,24],"641":[41,26,41,32],"649":[41,34,41,39],"657":[41,11,41,40],"665":[41,11,41,40],"673":[41,3,41,40],"681":[43,1,43,8],"689":[43,13,43,40],"697":[43,42,43,47],"705":[43,1,43,48],"707":[43,1,43,12],"713":[43,1,43,48],"721":[45,1,45,8],"729":[45,13,45,33],"737":[45,1,45,34],"739":[45,1,45,12],"745":[45,1,45,34],"753":[46,1,46,8],"761":[46,13,46,42],"769":[46,1,46,43],"771":[46,1,46,12],"777":[46,1,46,43],"785":[47,1,47,8],"793":[47,13,47,24],"801":[47,25,47,31],"809":[47,33,47,39],"817":[47,41,47,46],"825":[47,13,47,47],"833":[47,1,47,48],"835":[47,1,47,12],"841":[47,1,47,48],"849":[1,1,50,1],"857":[1,1,50,1],"865":[1,1,50,1],"873":[1,1,50,1],"881":[14,10,16,2],"889":[14,10,16,2],"897":[17,15,19,2],"905":[17,15,19,2],"913":[29,1,34,2],"921":[40,1,42,2],"929":[1,1,50,1],"937":[1,1,50,1],"nBranches":4,"originalCodeFileName":"/Users/tzuhan/+research/hyper_enforce/model_builder/jalangi2/hyperenforce/mytest_suppress_enforced.js","instrumentedCodeFileName":"/Users/tzuhan/+research/hyper_enforce/model_builder/jalangi2/hyperenforce/mytest_suppress_enforced_jalangi_.js","code":"/* Copyright (c) Royal Holloway, University of London | Contact Blake Loring (blake@parsed.uk), Duncan Mitchell (Duncan.Mitchell.2015@rhul.ac.uk), or Johannes Kinder (johannes.kinder@rhul.ac.uk) for details or support | LICENSE.md for license details */\n// var S$ = require('S$');\n\n/* SYMBOLIC VARS */\nvar ucon_x;\nvar ucon_z;\nvar con_y;\n\nucon_x = true; ucon_z = true; con_y = true;\n //if z is true, we suppress, if false we don't\n // no matter x us true or false\n\n/* added functions by the controller */\nsupp_0 = function (ucon_x, ucon_z, con_y) {\n  console.log('decide to suppress or not')\n}\ncheckvalues = function (ucon_x, ucon_z, con_y){\n  // debuging check\n}\n\n/* MAIN JS PROGRAM */\n///\nconsole.log('------------------')\nconsole.log('step 0: initial values')\nconsole.log(checkvalues(ucon_x, ucon_z, con_y))\n///\nconsole.log('------------------')\nconsole.log('step 1: if(z)-then-x-is-true')\nif(ucon_z){\n  ucon_x = true\n}\nelse{\n  ucon_x = false\n}\nconsole.log(checkvalues(ucon_x, ucon_z, con_y))\n///\nconsole.log('------------------')\nconsole.log('step 2: if(x)-then-y-is-false')\n// result = ''\nif(ucon_x){\n  con_y = supp_0(ucon_x, ucon_z, con_y)\n}\nconsole.log('after a controllable op: ', con_y)\n///\nconsole.log('------------------')\nconsole.log('step 3: final return values')\nconsole.log(checkvalues(ucon_x, ucon_z, con_y))\n\n/// END OF FILE ///\n"};
jalangiLabel2:
    while (true) {
        try {
            J$.Se(849, '/Users/tzuhan/+research/hyper_enforce/model_builder/jalangi2/hyperenforce/mytest_suppress_enforced_jalangi_.js', '/Users/tzuhan/+research/hyper_enforce/model_builder/jalangi2/hyperenforce/mytest_suppress_enforced.js');
            J$.N(857, 'ucon_x', ucon_x, 0);
            J$.N(865, 'ucon_z', ucon_z, 0);
            J$.N(873, 'con_y', con_y, 0);
            var ucon_x;
            var ucon_z;
            var con_y;
            J$.X1(25, ucon_x = J$.W(17, 'ucon_x', J$.T(9, true, 23, false), ucon_x, 2));
            J$.X1(49, ucon_z = J$.W(41, 'ucon_z', J$.T(33, true, 23, false), ucon_z, 2));
            J$.X1(73, con_y = J$.W(65, 'con_y', J$.T(57, true, 23, false), con_y, 2));
            J$.X1(169, supp_0 = J$.W(161, 'supp_0', J$.T(153, function (ucon_x, ucon_z, con_y) {
                jalangiLabel0:
                    while (true) {
                        try {
                            J$.Fe(113, arguments.callee, this, arguments);
                            arguments = J$.N(121, 'arguments', arguments, 4);
                            ucon_x = J$.N(129, 'ucon_x', ucon_x, 4);
                            ucon_z = J$.N(137, 'ucon_z', ucon_z, 4);
                            con_y = J$.N(145, 'con_y', con_y, 4);
                            J$.X1(105, J$.M(97, J$.R(81, 'console', console, 2), 'log', 0)(J$.T(89, 'decide to suppress or not', 21, false)));
                        } catch (J$e) {
                            J$.Ex(881, J$e);
                        } finally {
                            if (J$.Fr(889))
                                continue jalangiLabel0;
                            else
                                return J$.Ra();
                        }
                    }
            }, 12, false, 113), J$.I(typeof supp_0 === 'undefined' ? undefined : supp_0), 4));
            J$.X1(233, checkvalues = J$.W(225, 'checkvalues', J$.T(217, function (ucon_x, ucon_z, con_y) {
                jalangiLabel1:
                    while (true) {
                        try {
                            J$.Fe(177, arguments.callee, this, arguments);
                            arguments = J$.N(185, 'arguments', arguments, 4);
                            ucon_x = J$.N(193, 'ucon_x', ucon_x, 4);
                            ucon_z = J$.N(201, 'ucon_z', ucon_z, 4);
                            con_y = J$.N(209, 'con_y', con_y, 4);
                        } catch (J$e) {
                            J$.Ex(897, J$e);
                        } finally {
                            if (J$.Fr(905))
                                continue jalangiLabel1;
                            else
                                return J$.Ra();
                        }
                    }
            }, 12, false, 177), J$.I(typeof checkvalues === 'undefined' ? undefined : checkvalues), 4));
            J$.X1(265, J$.M(257, J$.R(241, 'console', console, 2), 'log', 0)(J$.T(249, '------------------', 21, false)));
            J$.X1(297, J$.M(289, J$.R(273, 'console', console, 2), 'log', 0)(J$.T(281, 'step 0: initial values', 21, false)));
            J$.X1(361, J$.M(353, J$.R(305, 'console', console, 2), 'log', 0)(J$.F(345, J$.R(313, 'checkvalues', checkvalues, 2), 0)(J$.R(321, 'ucon_x', ucon_x, 1), J$.R(329, 'ucon_z', ucon_z, 1), J$.R(337, 'con_y', con_y, 1))));
            J$.X1(393, J$.M(385, J$.R(369, 'console', console, 2), 'log', 0)(J$.T(377, '------------------', 21, false)));
            J$.X1(425, J$.M(417, J$.R(401, 'console', console, 2), 'log', 0)(J$.T(409, 'step 1: if(z)-then-x-is-true', 21, false)));
            if (J$.X1(913, J$.C(8, J$.R(433, 'ucon_z', ucon_z, 1)))) {
                J$.X1(457, ucon_x = J$.W(449, 'ucon_x', J$.T(441, true, 23, false), ucon_x, 2));
            } else {
                J$.X1(481, ucon_x = J$.W(473, 'ucon_x', J$.T(465, false, 23, false), ucon_x, 2));
            }
            J$.X1(545, J$.M(537, J$.R(489, 'console', console, 2), 'log', 0)(J$.F(529, J$.R(497, 'checkvalues', checkvalues, 2), 0)(J$.R(505, 'ucon_x', ucon_x, 1), J$.R(513, 'ucon_z', ucon_z, 1), J$.R(521, 'con_y', con_y, 1))));
            J$.X1(577, J$.M(569, J$.R(553, 'console', console, 2), 'log', 0)(J$.T(561, '------------------', 21, false)));
            J$.X1(609, J$.M(601, J$.R(585, 'console', console, 2), 'log', 0)(J$.T(593, 'step 2: if(x)-then-y-is-false', 21, false)));
            if (J$.X1(921, J$.C(16, J$.R(617, 'ucon_x', ucon_x, 1)))) {
                J$.X1(673, con_y = J$.W(665, 'con_y', J$.F(657, J$.R(625, 'supp_0', supp_0, 2), 0)(J$.R(633, 'ucon_x', ucon_x, 1), J$.R(641, 'ucon_z', ucon_z, 1), J$.R(649, 'con_y', con_y, 1)), con_y, 2));
            }
            J$.X1(713, J$.M(705, J$.R(681, 'console', console, 2), 'log', 0)(J$.T(689, 'after a controllable op: ', 21, false), J$.R(697, 'con_y', con_y, 1)));
            J$.X1(745, J$.M(737, J$.R(721, 'console', console, 2), 'log', 0)(J$.T(729, '------------------', 21, false)));
            J$.X1(777, J$.M(769, J$.R(753, 'console', console, 2), 'log', 0)(J$.T(761, 'step 3: final return values', 21, false)));
            J$.X1(841, J$.M(833, J$.R(785, 'console', console, 2), 'log', 0)(J$.F(825, J$.R(793, 'checkvalues', checkvalues, 2), 0)(J$.R(801, 'ucon_x', ucon_x, 1), J$.R(809, 'ucon_z', ucon_z, 1), J$.R(817, 'con_y', con_y, 1))));
        } catch (J$e) {
            J$.Ex(929, J$e);
        } finally {
            if (J$.Sr(937)) {
                J$.L();
                continue jalangiLabel2;
            } else {
                J$.L();
                break jalangiLabel2;
            }
        }
    }
// JALANGI DO NOT INSTRUMENT
