str1='sarika'
for ch in str1:
    s1=(ord(ch)&127)
    s2=(ord(ch)|127)
    s3=(ord(ch)^127)
    print(ch+'&127'+chr(s1)+'\t'+
          ch+'|127'+chr(s2)+'\t'+
          ch+'^127'+chr(s3)+'\t' )














#str1="teju"
#for ch in str1:
    #s1=(ord(ch)&127)
    #s2=(ord(ch)|127)
    #s3=(ord(ch)^127)
    #print(ch+'&127:'+chr(s1)+'\t'+
          #ch+'|127:'+chr(s2)+'\t'+
          #ch+'^127:'+chr(s3)+'\t')
