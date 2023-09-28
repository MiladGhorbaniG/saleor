
# Saleor Custom Product Attributes Documentation

Welcome to the Saleor Custom Product Attributes documentation. This guide will help you understand how to create, manage, and use custom product attributes in Saleor to enhance your e-commerce store.

**Table of Contents**

1. [Introduction](#introduction)
2. [Creating Custom Attributes](#creating-custom-attributes)
3. [Editing Custom Attributes](#editing-custom-attributes)
4. [Deleting Custom Attributes](#deleting-custom-attributes)
5. [Using Custom Attributes](#using-custom-attributes)
6. [Permissions and Security](#permissions-and-security)
7. [Examples](#examples)

## Introduction

Saleor allows you to define custom attributes for your products and product variants, providing flexibility in describing and categorizing your products. Custom attributes can include information such as product material, color options, size variations, and more.

## Creating Custom Attributes

To create a custom attribute:

1. Log in to your Saleor admin panel.
2. Navigate to the "Products" section.
3. Click on "Custom Attributes."
4. Click the "Add Custom Attribute" button.
5. Fill in the required information:
   - **Name:** Enter the name of the attribute (e.g., "Material," "Color").
   - **Slug:** Provide a unique slug for the attribute (e.g., "material," "color").
   - **Input Type:** Choose the input type for the attribute (e.g., "DROPDOWN," "NUMERIC," "TEXT").
   - **Entity Type:** Select whether the attribute applies to "PRODUCT" or "VARIANT."
   - **Unit:** If applicable, specify the unit of measurement (e.g., "cm," "inches").
6. Click "Save" to create the custom attribute.

## Editing Custom Attributes

To edit a custom attribute:

1. Log in to your Saleor admin panel.
2. Navigate to the "Products" section.
3. Click on "Custom Attributes."
4. Locate the custom attribute you want to edit and click on it.
5. Update the attribute details as needed, such as the name, slug, input type, entity type, or unit.
6. Click "Save" to apply the changes.

## Deleting Custom Attributes

To delete a custom attribute:

1. Log in to your Saleor admin panel.
2. Navigate to the "Products" section.
3. Click on "Custom Attributes."
4. Locate the custom attribute you want to delete and click on it.
5. Click the "Delete" button.
6. Confirm the deletion when prompted.

**Note:** Only authorized users with the necessary permissions can delete custom attributes.

## Using Custom Attributes

Custom attributes can be used in various ways:

- **Product Details:** Assign custom attributes to products to provide additional information to customers.
- **Variant Options:** Use custom attributes to define variant options such as size, color, and material.
- **Filters:** Create product filters based on custom attributes to help customers find products easily.
- **GraphQL API:** Access and retrieve custom attributes programmatically using Saleor's GraphQL API.

## Permissions and Security

Saleor ensures proper permissions and security when working with custom attributes. Admin users can create, edit, and delete custom attributes based on their roles and permissions. Unauthorized access is restricted, and the GraphQL API enforces access controls.

## Examples

For more usage examples and detailed scenarios, please refer to our [Custom Product Attributes Examples](docs/custom_attributes_examples.md).

---

This documentation provides a comprehensive guide to creating, managing, and using custom product attributes in Saleor. For additional information and technical details, consult the official Saleor documentation.

If you have any questions or need assistance, feel free to reach out to our support team.

**Happy selling with Saleor!**
