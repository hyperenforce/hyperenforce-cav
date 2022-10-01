J$.iids = {"8":[17,13,17,22],"9":[4,10,4,17],"10":[10,18,10,25],"16":[12,9,12,15],"17":[4,18,4,22],"18":[12,9,12,15],"24":[22,9,22,15],"25":[4,10,4,23],"26":[14,19,14,21],"32":[42,9,42,45],"33":[4,10,4,23],"34":[17,13,17,22],"40":[42,9,42,45],"41":[4,10,4,23],"42":[18,22,18,29],"49":[8,5,8,12],"50":[22,9,22,15],"57":[8,17,8,30],"58":[42,9,42,25],"65":[8,32,8,34],"66":[42,29,42,45],"73":[8,36,8,41],"74":[43,19,43,42],"81":[8,43,8,45],"89":[8,5,8,46],"91":[8,5,8,16],"97":[8,5,8,47],"105":[10,18,10,20],"113":[10,23,10,25],"121":[10,18,10,25],"129":[10,18,10,25],"137":[12,9,12,11],"145":[12,14,12,15],"153":[13,9,13,16],"161":[13,21,13,36],"169":[13,9,13,37],"171":[13,9,13,20],"177":[13,9,13,38],"185":[14,19,14,21],"193":[14,9,14,15],"201":[14,9,14,21],"209":[14,9,14,22],"217":[16,9,16,16],"225":[16,21,16,36],"233":[16,9,16,37],"235":[16,9,16,20],"241":[16,9,16,38],"249":[17,13,17,15],"257":[17,19,17,22],"265":[18,23,18,29],"273":[18,22,18,29],"281":[18,13,18,30],"289":[22,9,22,11],"297":[22,14,22,15],"305":[23,9,23,16],"313":[23,21,23,36],"321":[23,9,23,37],"323":[23,9,23,20],"329":[23,9,23,38],"337":[25,9,25,16],"345":[25,21,25,36],"353":[25,9,25,37],"355":[25,9,25,20],"361":[25,9,25,38],"369":[28,5,28,12],"377":[28,17,28,30],"385":[28,32,28,38],"393":[28,5,28,39],"395":[28,5,28,16],"401":[28,5,28,40],"409":[30,12,30,18],"417":[30,12,30,18],"425":[30,5,30,19],"433":[6,1,31,2],"441":[6,1,31,2],"449":[6,1,31,2],"457":[6,1,31,2],"465":[6,1,31,2],"473":[35,19,35,21],"481":[35,29,35,33],"489":[35,35,35,36],"497":[35,19,35,37],"499":[35,19,35,28],"505":[35,19,35,37],"513":[35,19,35,37],"521":[36,20,36,22],"529":[36,30,36,35],"537":[36,37,36,39],"545":[36,20,36,40],"547":[36,20,36,29],"553":[36,20,36,40],"561":[36,20,36,40],"569":[37,20,37,22],"577":[37,30,37,35],"585":[37,37,37,39],"593":[37,20,37,40],"595":[37,20,37,29],"601":[37,20,37,40],"609":[37,20,37,40],"617":[39,21,39,22],"625":[39,23,39,30],"633":[39,32,39,40],"641":[39,21,39,41],"649":[39,21,39,41],"657":[39,21,39,41],"665":[40,21,40,22],"673":[40,23,40,30],"681":[40,32,40,40],"689":[40,21,40,41],"697":[40,21,40,41],"705":[40,21,40,41],"713":[42,9,42,17],"721":[42,22,42,25],"729":[42,29,42,37],"737":[42,42,42,45],"745":[43,9,43,11],"753":[43,19,43,28],"761":[43,33,43,42],"769":[43,9,43,43],"771":[43,9,43,18],"777":[43,9,43,44],"785":[33,1,45,2],"793":[33,1,45,2],"801":[33,1,45,2],"809":[33,1,45,2],"817":[33,1,45,2],"825":[33,1,45,2],"833":[33,1,45,2],"841":[33,1,45,2],"849":[47,1,47,7],"857":[47,8,47,16],"865":[47,1,47,17],"873":[47,1,47,18],"881":[1,1,47,18],"889":[1,1,47,18],"897":[6,1,31,2],"905":[1,1,47,18],"913":[33,1,45,2],"921":[1,1,47,18],"929":[17,9,19,10],"937":[12,5,20,6],"945":[22,5,26,6],"953":[6,1,31,2],"961":[6,1,31,2],"969":[42,5,44,6],"977":[33,1,45,2],"985":[33,1,45,2],"993":[1,1,47,18],"1001":[1,1,47,18],"nBranches":10,"originalCodeFileName":"/Users/tzuhan/+research/hyper_enforce/tzuhan/ExpoSE-master/mytests/infoflow.js","instrumentedCodeFileName":"/Users/tzuhan/+research/hyper_enforce/tzuhan/ExpoSE-master/mytests/infoflow_jalangi_.js","code":"/* Copyright (c) Royal Holloway, University of London | Contact Blake Loring (blake@parsed.uk), Duncan Mitchell (Duncan.Mitchell.2015@rhul.ac.uk), or Johannes Kinder (johannes.kinder@rhul.ac.uk) for details or support | LICENSE.md for license details */\n\n\"use strict\";\n\nvar S$ = require('S$');\n\nfunction flowTest(lo, hi) {\n\n    console.log(\"Inputs: Hi:\", hi, \"Lo:\", lo);\n\n    var result = lo * 42;\n\n    if (lo > 4) {\n        console.log(\"Branch A-then\");\n        result -= lo;\n    } else {\n        console.log(\"Branch A-else\");\n        if (hi == 777) {\n            result = -result;\n        }\n    }\n\n    if (hi > 0) {\n        console.log(\"Branch B-then\");\n    } else {\n        console.log(\"Branch B-else\");\n    }\n\n    console.log(\"Low output:\", result);\n\n    return result;\n}\n\nfunction verify(f) {\n\n    var loInput = S$.symbol('LO', 0);\n    var hiInput1 = S$.symbol('HI1', 10);\n    var hiInput2 = S$.symbol('HI2', 10);\n\n    var loOutput1 = f(loInput, hiInput1);\n    var loOutput2 = f(loInput, hiInput2);\n\n    if (hiInput1 !== 777 && hiInput2 !== 777) {\n        S$.assert(loOutput1 === loOutput2);\n    }\n}\n\nverify(flowTest);\n"};
jalangiLabel2:
    while (true) {
        try {
            J$.Se(881, '/Users/tzuhan/+research/hyper_enforce/tzuhan/ExpoSE-master/mytests/infoflow_jalangi_.js', '/Users/tzuhan/+research/hyper_enforce/tzuhan/ExpoSE-master/mytests/infoflow.js');
            function flowTest(lo, hi) {
                jalangiLabel0:
                    while (true) {
                        try {
                            J$.Fe(433, arguments.callee, this, arguments);
                            arguments = J$.N(441, 'arguments', arguments, 4);
                            lo = J$.N(449, 'lo', lo, 4);
                            hi = J$.N(457, 'hi', hi, 4);
                            J$.N(465, 'result', result, 0);
                            J$.X1(97, J$.M(89, J$.R(49, 'console', console, 2), 'log', 0)(J$.T(57, "Inputs: Hi:", 21, false), J$.R(65, 'hi', hi, 0), J$.T(73, "Lo:", 21, false), J$.R(81, 'lo', lo, 0)));
                            var result = J$.X1(129, J$.W(121, 'result', J$.B(10, '*', J$.R(105, 'lo', lo, 0), J$.T(113, 42, 22, false), 0), result, 1));
                            if (J$.X1(937, J$.C(16, J$.B(18, '>', J$.R(137, 'lo', lo, 0), J$.T(145, 4, 22, false), 0)))) {
                                J$.X1(177, J$.M(169, J$.R(153, 'console', console, 2), 'log', 0)(J$.T(161, "Branch A-then", 21, false)));
                                J$.X1(209, result = J$.W(201, 'result', J$.B(26, '-', J$.R(193, 'result', result, 0), J$.R(185, 'lo', lo, 0), 0), result, 0));
                            } else {
                                J$.X1(241, J$.M(233, J$.R(217, 'console', console, 2), 'log', 0)(J$.T(225, "Branch A-else", 21, false)));
                                if (J$.X1(929, J$.C(8, J$.B(34, '==', J$.R(249, 'hi', hi, 0), J$.T(257, 777, 22, false), 0)))) {
                                    J$.X1(281, result = J$.W(273, 'result', J$.U(42, '-', J$.R(265, 'result', result, 0)), result, 0));
                                }
                            }
                            if (J$.X1(945, J$.C(24, J$.B(50, '>', J$.R(289, 'hi', hi, 0), J$.T(297, 0, 22, false), 0)))) {
                                J$.X1(329, J$.M(321, J$.R(305, 'console', console, 2), 'log', 0)(J$.T(313, "Branch B-then", 21, false)));
                            } else {
                                J$.X1(361, J$.M(353, J$.R(337, 'console', console, 2), 'log', 0)(J$.T(345, "Branch B-else", 21, false)));
                            }
                            J$.X1(401, J$.M(393, J$.R(369, 'console', console, 2), 'log', 0)(J$.T(377, "Low output:", 21, false), J$.R(385, 'result', result, 0)));
                            return J$.X1(425, J$.Rt(417, J$.R(409, 'result', result, 0)));
                        } catch (J$e) {
                            J$.Ex(953, J$e);
                        } finally {
                            if (J$.Fr(961))
                                continue jalangiLabel0;
                            else
                                return J$.Ra();
                        }
                    }
            }
            function verify(f) {
                jalangiLabel1:
                    while (true) {
                        try {
                            J$.Fe(785, arguments.callee, this, arguments);
                            arguments = J$.N(793, 'arguments', arguments, 4);
                            f = J$.N(801, 'f', f, 4);
                            J$.N(809, 'loInput', loInput, 0);
                            J$.N(817, 'hiInput1', hiInput1, 0);
                            J$.N(825, 'hiInput2', hiInput2, 0);
                            J$.N(833, 'loOutput1', loOutput1, 0);
                            J$.N(841, 'loOutput2', loOutput2, 0);
                            var loInput = J$.X1(513, J$.W(505, 'loInput', J$.M(497, J$.R(473, 'S$', S$, 1), 'symbol', 0)(J$.T(481, 'LO', 21, false), J$.T(489, 0, 22, false)), loInput, 1));
                            var hiInput1 = J$.X1(561, J$.W(553, 'hiInput1', J$.M(545, J$.R(521, 'S$', S$, 1), 'symbol', 0)(J$.T(529, 'HI1', 21, false), J$.T(537, 10, 22, false)), hiInput1, 1));
                            var hiInput2 = J$.X1(609, J$.W(601, 'hiInput2', J$.M(593, J$.R(569, 'S$', S$, 1), 'symbol', 0)(J$.T(577, 'HI2', 21, false), J$.T(585, 10, 22, false)), hiInput2, 1));
                            var loOutput1 = J$.X1(657, J$.W(649, 'loOutput1', J$.F(641, J$.R(617, 'f', f, 0), 0)(J$.R(625, 'loInput', loInput, 0), J$.R(633, 'hiInput1', hiInput1, 0)), loOutput1, 1));
                            var loOutput2 = J$.X1(705, J$.W(697, 'loOutput2', J$.F(689, J$.R(665, 'f', f, 0), 0)(J$.R(673, 'loInput', loInput, 0), J$.R(681, 'hiInput2', hiInput2, 0)), loOutput2, 1));
                            if (J$.X1(969, J$.C(40, J$.C(32, J$.B(58, '!==', J$.R(713, 'hiInput1', hiInput1, 0), J$.T(721, 777, 22, false), 0)) ? J$.B(66, '!==', J$.R(729, 'hiInput2', hiInput2, 0), J$.T(737, 777, 22, false), 0) : J$._()))) {
                                J$.X1(777, J$.M(769, J$.R(745, 'S$', S$, 1), 'assert', 0)(J$.B(74, '===', J$.R(753, 'loOutput1', loOutput1, 0), J$.R(761, 'loOutput2', loOutput2, 0), 0)));
                            }
                        } catch (J$e) {
                            J$.Ex(977, J$e);
                        } finally {
                            if (J$.Fr(985))
                                continue jalangiLabel1;
                            else
                                return J$.Ra();
                        }
                    }
            }
            J$.N(889, 'S$', S$, 0);
            flowTest = J$.N(905, 'flowTest', J$.T(897, flowTest, 12, false, 433), 0);
            verify = J$.N(921, 'verify', J$.T(913, verify, 12, false, 785), 0);
            var S$ = J$.X1(41, J$.W(33, 'S$', J$.F(25, J$.R(9, 'require', require, 2), 0)(J$.T(17, 'S$', 21, false)), S$, 3));
            J$.X1(873, J$.F(865, J$.R(849, 'verify', verify, 1), 0)(J$.R(857, 'flowTest', flowTest, 1)));
        } catch (J$e) {
            J$.Ex(993, J$e);
        } finally {
            if (J$.Sr(1001)) {
                J$.L();
                continue jalangiLabel2;
            } else {
                J$.L();
                break jalangiLabel2;
            }
        }
    }
// JALANGI DO NOT INSTRUMENT
