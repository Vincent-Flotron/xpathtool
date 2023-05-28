import argparse
import logging
import datetime
import csv
from lxml import etree


def perform_xpath_query(input_xml, xpath_query):
    # Parse the XML file
    tree = etree.parse(input_xml)

    # Perform the XPath query
    result = tree.xpath(xpath_query)

    return result


def setup_logging():
    # Configure the logging format
    log_format = "%(message)s"
    logging.basicConfig(filename='xpath-queries.log', level=logging.INFO, format=log_format)


def log_query_result(xpath_query, result):
    # Log the query and result
    logging.info(f"{datetime.datetime.now()};{xpath_query};{result}")


def display_history(hist_file):
    # Display the history of all XPath requests
    with open(hist_file, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            print(row[1])


def display_successful_history(hist_file):
    # Display the history of successful XPath requests
    with open(hist_file, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row[2] != '':
                print(row[1])


def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Perform XPath query on an XML file.")
    parser.add_argument("input_xml", nargs='?', help="XML file to query")
    parser.add_argument("xpath_query", nargs='?', help="XPath query to perform")
    parser.add_argument("-l", "--hist", action="store_true", help="Display history of all XPath requests")
    parser.add_argument("-w", "--worked", action="store_true", help="Display history of successful XPath requests")
    args = parser.parse_args()
    # args.hist = True
    args.worked = True
    # Set up logging
    setup_logging()

    if args.hist:
        display_history("xpath-queries.log")
    elif args.worked:
        display_successful_history("xpath-queries.log")
    else:
        # Check if input_xml and xpath_query are provided
        if not args.input_xml or not args.xpath_query:
            parser.error("The following arguments are required: input_xml, xpath_query")
        
        # Perform the XPath query
        result = perform_xpath_query(args.input_xml, args.xpath_query)

        # Convert the result to a human-readable format
        res = ""
        for element in result:
            res += etree.tostring(element, encoding="unicode")

        # Display the result
        print(f"XPath query: {args.xpath_query}")
        print("XPath query result:")
        print(res)

        # Log the query and result
        log_query_result(args.xpath_query, res.replace("\n", "\\n"))


if __name__ == "__main__":
    main()
