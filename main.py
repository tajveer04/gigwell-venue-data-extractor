                directory_fifth_phone = ""
                directory_fifth_email = ""
                directory_sixth = ""
                directory_sixth_title = ""
                directory_sixth_phone = ""
                directory_sixth_email = ""
                directory_seventh = ""
                directory_seventh_title = ""
                directory_seventh_phone = ""
                directory_seventh_email = ""

                # Fetch all the required details for the venue
                try:
                    venue_name = driver.find_element(By.XPATH, "//div[@class='venue-header-content-inner']//p[1]").text
                except Exception:
                    pass
                try:
                    venue_address = driver.find_element(By.XPATH, "//div[@class='venue-header-content-inner']//p[2]").text
                except Exception:
                    pass
                try:
                    venue_email = driver.find_element(By.XPATH, "//div[@class='venue-header-content-inner']//p[3]/a").text
                except Exception:
                    pass
                try:
                    venue_phone = driver.find_element(By.XPATH, "//div[@class='venue-header-content-inner']//p[3]/span").text
                except Exception:
                    pass
                try:
                    venue_capacity = driver.find_element(By.XPATH, "//div[@class='stat'][1]/span[@class='stat-number']").text
                except Exception:
                    pass
                try:
                    venue_avg_tix_sold = driver.find_element(By.XPATH, "//div[@class='stat'][2]/span[@class='stat-number']").text
                except Exception:
                    pass

                # Fetch directory contacts
                for i in range(1, 8):  # Loop through 7 possible contacts
                    try:
                        contact_name = driver.find_element(By.XPATH, f"//ul[@class='list-unstyled venue-directory-list']/li[{i}]/div[@class='venue-directory-contact']/p[1]").text
                        contact_title = driver.find_element(By.XPATH, f"//ul[@class='list-unstyled venue-directory-list']/li[{i}]/div[@class='venue-directory-contact']/p[3]").text
                        contact_phone = driver.find_element(By.XPATH, f"//ul[@class='list-unstyled venue-directory-list']/li[{i}]/div[@class='venue-directory-contact']/p[4]").text
                        contact_email = driver.find_element(By.XPATH, f"//ul[@class='list-unstyled venue-directory-list']/li[{i}]/div[@class='venue-directory-contact']/p[5]").text

                        # Assign values to the respective directory variables
                        if i == 1:
                            directory_first = contact_name
                            directory_first_title = contact_title
                            directory_first_phone = contact_phone
                            directory_first_email = contact_email
                        elif i == 2:
                            directory_second = contact_name
                            directory_second_title = contact_title
                            directory_second_phone = contact_phone
                            directory_second_email = contact_email
                        elif i == 3:
                            directory_third = contact_name
                            directory_third_title = contact_title
                            directory_third_phone = contact_phone
                            directory_third_email = contact_email
                        elif i == 4:
                            directory_forth = contact_name
                            directory_forth_title = contact_title
                            directory_forth_phone = contact_phone
                            directory_forth_email = contact_email
                        elif i == 5:
                            directory_fifth = contact_name
                            directory_fifth_title = contact_title
                            directory_fifth_phone = contact_phone
                            directory_fifth_email = contact_email
                        elif i == 6:
                            directory_sixth = contact_name
                            directory_sixth_title = contact_title
                            directory_sixth_phone = contact_phone
                            directory_sixth_email = contact_email
                        elif i == 7:
                            directory_seventh = contact_name
                            directory_seventh_title = contact_title
                            directory_seventh_phone = contact_phone
                            directory_seventh_email = contact_email
                    except Exception:
                        # If any contact details are missing, skip to the next contact
                        continue

                # Write data to CSV
                writer.writerow([
                    venue_name, venue_address, venue_email, venue_phone, venue_capacity, venue_avg_tix_sold,
                    directory_first, directory_first_title, directory_first_phone, directory_first_email,
                    directory_second, directory_second_title, directory_second_phone, directory_second_email,
                    directory_third, directory_third_title, directory_third_phone, directory_third_email,
                    directory_forth, directory_forth_title, directory_forth_phone, directory_forth_email,
                    directory_fifth, directory_fifth_title, directory_fifth_phone, directory_fifth_email,
                    directory_sixth, directory_sixth_title, directory_sixth_phone, directory_sixth_email,
                    directory_seventh, directory_seventh_title, directory_seventh_phone, directory_seventh_email
                ])

                # Go back to the venue list
                driver.back()
                time.sleep(5)
        except Exception as e:
            print(f"Error fetching venue details: {e}")

    # Pagination handling: Loop through all pages
    while True:
        process_venues()
        try:
            # Attempt to find and click the "Next" button
            next_button = driver.find_element(By.XPATH, "//button[@class='btn-icon-absolute venue-portal-search-results-pagination-right']")
            next_button.click()
            print("Navigating to the next page...")
            time.sleep(5)  # Wait for the next page to load
        except Exception:
            print("No more pages found. Scraping complete.")
            break  # Exit the loop if "Next" button is not found

# Close the browser
driver.quit()




