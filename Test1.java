public class Test5 { 
        private static int a; 
        private int b;
        static { 
                Test5.a = 3; 
                System.out.println(a); 
                Test5 t = new Test5(); 
                t.f(); 
                t.b = 1000; 
                System.out.println(t.b); 
        }
        static { 
                Test5.a = 4; 
                System.out.println(a); 
        }
        public static void main(String[] args) { 
                // 
                //         }
                //                 static { 
                //                                 Test5.a = 5; 
                //                                                 System.out.println(a); 
                //                                                         } 
                //                                                                 public void f() { 
                //                                                                                 System.out.println("hhahhahah"); 
                //                                                                                         } 
                //
                //                                                                                          }:
