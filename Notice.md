COMPANY_NAME, COMPANY_NUMBER, USER NAME, ADDRESS
//*[@class="heading-xlarge"] |
//*[@id="company-number"]/strong | 
//*[@class="appointments-list"]/div/h2 |
//*[@class="appointments-list"]/div/dl 



COMPANY_NAME, NUMBER, FULL INFO DIV


//*[@class="heading-xlarge"] |
//*[@id="company-number"]/strong | 
//*[@class="appointments-list"]/div 

concat('COMPANY_NAME:',//*[normalize-space(@class)="heading-xlarge"])
concat('NAME:',//*[normalize-space(@id)="company-number"])
concat('COMPANY_NAME:',//*[normalize-space(@class)="heading-xlarge"])


concat("COMPANY_NAME:",//*[normalize-space(@class)="heading-xlarge"] ,"\n COMPANY_NUMBER:",//*[normalize-space(@id)="company-number"]/strong)