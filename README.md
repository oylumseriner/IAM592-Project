# IAM592-Project-Sbox and AES
Hi everyone, I prepare the S-Box project for IAM 592 Introduction to Programming II. You can find explaination of code.  
### Example of Boolean:
I try to show one example about Boolean function, this example of code shows that Truth Table,Non linearity,Non homomoprpicity,Correlation immunity and Propogation characteristics of f.\
0  &  1  &  2 &  3   & 4  & 5  & 6 & 7 & 8 & 9 & 10 & 11 & 12 & 13 & 14 & 15 \
46 &  10 &  3 &  15  & 48 & 60 & 22& 43& 50& 2 & 50 & 30 & 13 & 38 & 58 & 7 \
First of all, we calculate the truth table of $\beta S(x)$ by using all $B\in V_6$ and $f1,f2,f3,f4,f5,f6$. Then, we compute the truth table of $ax$ and compare them. So, we create the LAT.\
### Example of S-box:
In cryptography, an S-box (substitution-box) is a basic component of symmetric key algorithms which performs substitution. In block ciphers, they are typically used to obscure the relationship between the key and the ciphertext, thus ensuring Shannon's property of confusion. Mathematically, an S-box is a vectorial Boolean function.\
We have 4x6 S-Box,
##### In Boolean Library,
**1. convert_to_binary(size):**
  * This def provides to create the inputs for any n size of bollean function.You can enter the n and you can get the list of all n size inputs for binary form.

**2. convert_to_binary_given(size,results):**
  * This def provides to create the inputs for any n size of bollean function. This def works on given inputs.

**3. truth_table(f,string_convert2):** 
  * If you add the funciton, input size and list of inputs, you can reach the truth table of function. Remmeber that, your function should be def form. For example,
  * It means that x7 + x8 + x1x2 + x3x4 + x5x6 + x7x8 + x1x2x3x4 + x3x4x5x7

**4. non_linearity (f,affine,size,string_convert2):**
  * We use the this formula, Nf=min(min\ d(f,l_alpha),2^n-max d(f,l_alpha)). We compute the min and max value of d(f,l_alpha), then we choose the min value in all values.

**5. non_homo(f,size,string_convert2):**
  * It means that NH_f=prob(f(x + y) + f(x) + f(y)=0), then we apply this.
    
**6. correlation_im1(f,affine,size,string_convert2):**
  * We check the l_\alpha, the we start the wt(f)=1. d(f,l_{\alpha})=2^{n-1}. If we have the all restults are not 2**(size-1), we should stop.
   
**7. correlation_im2(f,affine,size,string_convert2):**
  * Remember that if the boolean function is corelation im 1, then check the correlation im 2. It cannot be best waoy for correlation, It should be improved.

**8. correlation_im3(f,affine,size,string_convert2):**

**9. xor(x,y)**:
  * This def providec clasical xor operations between two arrays.
    
**10. pc1(f,xor,size,string_convert2):**
  * We use the this equation |x:f(x + \alpha) = f(x)|=2^{n-1}.If there are equality between two results (Tf and outputs after XOR operation) and we can move the pc2. 

**11. pc2(f,xor,size,string_convert2):**
    
**12. pc3(f,xor,size,string_convert2):**
    
**13. LAT(alpha,betha,size):**
  * For example, we calculate the truth table of beta S(x) by using all V_6 and f1,f2,f3,f4,f5,f6. Then, we compute the truth table of ax and compare them. So, we create the LAT.

**14. convert_to_decimal(x):**
  * this provides binary convert to decimal numbers.



    
