# how to use 

cmake -B build -G "Visual Studio 16 2019"


cmake -B build -G "Visual Studio 17 2022"
- v143 툴셋 이슈 


calender


취업일
입대일
전역일
중소기업 취업한 날 연령
병역근무기간
병역근무기간 차감 후 연령
대상여부


가능





# 엑셀 수식 

주민번호 앞자리 입력 생년월일 
=DATE(LEFT(B4,2),MID(B4,3,2),MID(B4,5,2))


입사일 

군입대 
군 제대 

취업시 연령 
=DATEDIF(C4,D4,"Y")&"년 "&DATEDIF(C4,D4,"YM")&"개월 "&DATEDIF(C4,D4,"MD")+1&"일"


군복무 기간 
=DATEDIF(E4,F4,"Y")&"년 "&DATEDIF(E4,F4,"YM")&"개월 "&DATEDIF(E4,F4,"MD")+1&"일"



적용 연령 
=IF(E4="",G4,IF(AND(DATEDIF(C4,E4,"YM")+DATEDIF(F4,D4,"YM")>=12,(DATEDIF(C4,E4,"MD")+DATEDIF(F4,D4,"MD")>=30)),(DATEDIF(C4,E4,"Y")+DATEDIF(F4,D4,"Y")+1)&"년 "&((DATEDIF(C4,E4,"YM")+DATEDIF(F4,D4,"YM")-10))&"개월 "&(DATEDIF(C4,E4,"MD")+DATEDIF(F4,D4,"MD")-29)&"일",IF(AND(DATEDIF(C4,E4,"YM")+DATEDIF(F4,D4,"YM")<12,(DATEDIF(C4,E4,"MD")+DATEDIF(F4,D4,"MD")>=30)),(DATEDIF(C4,E4,"Y")+DATEDIF(F4,D4,"Y"))&"년 "&((DATEDIF(C4,E4,"YM")+DATEDIF(F4,D4,"YM")+1))&"개월 "&(DATEDIF(C4,E4,"MD")+DATEDIF(F4,D4,"MD")-29)&"일",IF(AND(DATEDIF(C4,E4,"YM")+DATEDIF(F4,D4,"YM")>=12,(DATEDIF(C4,E4,"MD")+DATEDIF(F4,D4,"MD")<30)),(DATEDIF(C4,E4,"Y")+DATEDIF(F4,D4,"Y")+1)&"년 "&((DATEDIF(C4,E4,"YM")+DATEDIF(F4,D4,"YM")-11))&"개월 "&(DATEDIF(C4,E4,"MD")+DATEDIF(F4,D4,"MD"))&"일",(DATEDIF(C4,E4,"Y")+DATEDIF(F4,D4,"Y"))&"년 "&(DATEDIF(C4,E4,"YM")+DATEDIF(F4,D4,"YM"))&"개월 "&(DATEDIF(C4,E4,"MD")+DATEDIF(F4,D4,"MD"))&"일"))))


대상여부 
=IF(VALUE(LEFT(I4,2))<30,"Y","N")