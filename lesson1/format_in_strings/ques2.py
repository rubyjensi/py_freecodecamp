'''Question 2: Movie Ticket Booking
Scenario: Ticket confirm hone ka message print karein.

Variables: movie_name = "Inception", tickets = 3, total_cost = 450

Expected Output: "Your booking for 3 tickets of the movie Inception is confirmed. Total amount paid is Rs. 450."'''

movie_name = "Inception"
tickets = 3
total_cost = 450 

output_template = "Your booking for {} tickets of the movie {} is confirmed. Total amount to be paid is {}"
output_message = output_template.format(tickets, movie_name, total_cost)
print(output_message)