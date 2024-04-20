import rtx_api.rtx_api_3_5 as rtx_api
import python_interface

def generate_company_descrption(company_name):
    return rtx_api.send_message(
        f"You are an talent aquisition professional trying to recruit people to your company {company_name}." +\
        f"Write a formal description of working at {company_name}, focusing on the company culture, work environment, " +\
        "benefits, team dynamics, and the technologies used. Provide a detailed and engaging insight into the unique " +\
        "aspects that make the company stand out.")

def gen_company_names(industries):
    companies = []
    for ind in industries:
        print(ind)
        tmp = python_interface.generate_list(f"Write a list of companies in the {ind} industry")
        print(tmp)
        companies += tmp
    companies = list(set(companies))
    return companies

def generate_description_to_all_companies_in_existence():
    industries = python_interface.generate_list("Write a list of all major industries")
    print(industries)
    companies = gen_company_names(industries)
    for corp in companies:
        desc = generate_company_descrption(corp)
        print('\n\n\n\n' + '-' * 20, corp, '-' * 20)
        print(desc)

if __name__ == '__main__':
    generate_description_to_all_companies_in_existence()
