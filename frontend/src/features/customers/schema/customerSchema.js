import { z } from "zod";

export const customerSchema = z.object({
  customer_code: z
    .string()
    .min(2, "Customer code is required"),

  name: z
    .string()
    .min(2, "Customer name is required"),

  company_name: z
    .string()
    .optional(),

  phone: z
    .string()
    .regex(/^[6-9]\d{9}$/, "Enter a valid 10-digit mobile number"),

  email: z
    .string()
    .email("Invalid email address")
    .or(z.literal("")),

  gst_number: z
    .string()
    .optional(),

  address: z
    .string()
    .optional(),
});