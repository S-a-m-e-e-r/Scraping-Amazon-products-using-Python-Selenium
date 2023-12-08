import selenium
from selenium import webdriver
import csv
from time import sleep
from lxml import html

#creating Firefox webdriver
driver=webdriver.Firefox()

#creating CSV file 
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    
    # Create a CSV writer
    csv_writer = csv.writer(csvfile)
    
    # Write the header row
    csv_writer.writerow(['Product_name', 'Product_price', 'Product_rating'])
    
    #loop to iterate through the different pages 
    for page_nb in range(1,6):

        #accessing amazon website through link
        #and page={}.format(pageno) is used to change page link of amazon
        driver.get("https://www.amazon.in/s?rh=n%3A6612025031&fs=true&ref=lp_6612025031_sar&page={}".format(page_nb))
        

        sleep(1)

        #creating tree to parse the amazon page 
        tree=html.fromstring(driver.page_source)
        
         # Loop through each div to extract information
        for product in tree.xpath("//div[@class='puis-card-container s-card-container s-overflow-hidden aok-relative puis-expand-height puis-include-content-margin puis puis-v1qlj3vrpms3m32klujlujtgcs8 s-latency-cf-section puis-card-border']"):

             # Find span with the specified class and  set Product_name 
            product_name=product.xpath(".//span[@class='a-size-base-plus a-color-base a-text-normal']/text()")[0]
            
            # Find span with the specified class and  set Product_price
            try:
                product_price=product.xpath(".//span[@class='a-price-whole']/text()")[0]
            except Exception as e:
                print(e)

            # Find span with the specified class and  set Product_rating 
            product_rating=product.xpath(".//span[@class='a-icon-alt']/text()")[0].split()[0]

            # Write the extracted information to the CSV file
            csv_writer.writerow([product_name, product_price, product_rating])

                    
# closing the driver
driver.close()
