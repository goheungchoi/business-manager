import { useMutation, gql } from "@apollo/client";

const CREATE_ADDRESS = gql`
mutation CreateAddress($input: AddressInput!) {
  createAddress(input: $input) {
    address {
      street
      city
      state
      country
      zip_code
    }
  }
}
`;

function CreateAddressForm() {
  let input;
  const [createAddress, { data, loading, error }] = useMutation(CREATE_ADDRESS);

  if (loading) return 'Submitting...';
  if (error) return `Submission error! ${error.message}`;

  return (
    <div>
      <form
        onSubmit={e => {
          e.preventDefault();
          createAddress({ variables: 
            { input: 
              {
                street: input.name.value,
                city: input.username.value,
                state: input.department.value,
                country: input.title.value,
                zip_code: input.role.value,
              }
            }
          });
          input = {};
        }}
      >
        <input
          ref={node => {
            input.street = node;
          }}
          placeholder="Street"
        />
        <input
          ref={node => {
            input.city = node;
          }}
          placeholder="City"
        />
        <input
          ref={node => {
            input.state = node;
          }}
          placeholder="State"
        />
        <input
          ref={node => {
            input.country = node;
          }}
          placeholder="Country"
        />
        <input
          ref={node => {
            input.zip_code = node;
          }}
          placeholder="Zip Code"
        />
        <button type="submit">Create Address</button>
      </form>
    </div>
  );
}

export default CreateAddressForm;
