# Databricks notebook source
remote_files = ["/ecommerce/", "/ecommerce/README.md", "/ecommerce/events/", "/ecommerce/events/events-1m.json/", "/ecommerce/events/events-1m.json/_SUCCESS", "/ecommerce/events/events-1m.json/_committed_6289868722686892311", "/ecommerce/events/events-1m.json/_started_6289868722686892311", "/ecommerce/events/events-1m.json/part-00000-tid-6289868722686892311-494bee2e-042e-46ab-b686-556a5ad5e3c1-2347-1-c000.json", "/ecommerce/events/events-2020-07-03.json/", "/ecommerce/events/events-2020-07-03.json/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=0/", "/ecommerce/events/events-2020-07-03.json/hour=0/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=0/_committed_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=0/_started_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=0/part-00000-tid-5790340178915489703-d0bf1a28-ced0-4475-890c-0836c456dacb-2353-1.c000.json", "/ecommerce/events/events-2020-07-03.json/hour=1/", "/ecommerce/events/events-2020-07-03.json/hour=1/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=1/_committed_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=1/_started_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=1/part-00000-tid-5790340178915489703-d0bf1a28-ced0-4475-890c-0836c456dacb-2353-2.c000.json", "/ecommerce/events/events-2020-07-03.json/hour=10/", "/ecommerce/events/events-2020-07-03.json/hour=10/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=10/_committed_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=10/_started_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=10/part-00000-tid-5790340178915489703-d0bf1a28-ced0-4475-890c-0836c456dacb-2353-11.c000.json", "/ecommerce/events/events-2020-07-03.json/hour=11/", "/ecommerce/events/events-2020-07-03.json/hour=11/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=11/_committed_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=11/_started_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=11/part-00000-tid-5790340178915489703-d0bf1a28-ced0-4475-890c-0836c456dacb-2353-12.c000.json", "/ecommerce/events/events-2020-07-03.json/hour=12/", "/ecommerce/events/events-2020-07-03.json/hour=12/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=12/_committed_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=12/_started_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=12/part-00000-tid-5790340178915489703-d0bf1a28-ced0-4475-890c-0836c456dacb-2353-13.c000.json", "/ecommerce/events/events-2020-07-03.json/hour=13/", "/ecommerce/events/events-2020-07-03.json/hour=13/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=13/_committed_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=13/_started_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=13/part-00000-tid-5790340178915489703-d0bf1a28-ced0-4475-890c-0836c456dacb-2353-14.c000.json", "/ecommerce/events/events-2020-07-03.json/hour=14/", "/ecommerce/events/events-2020-07-03.json/hour=14/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=14/_committed_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=14/_started_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=14/part-00000-tid-5790340178915489703-d0bf1a28-ced0-4475-890c-0836c456dacb-2353-15.c000.json", "/ecommerce/events/events-2020-07-03.json/hour=15/", "/ecommerce/events/events-2020-07-03.json/hour=15/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=15/_committed_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=15/_started_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=15/part-00000-tid-5790340178915489703-d0bf1a28-ced0-4475-890c-0836c456dacb-2353-16.c000.json", "/ecommerce/events/events-2020-07-03.json/hour=16/", "/ecommerce/events/events-2020-07-03.json/hour=16/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=16/_committed_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=16/_started_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=16/part-00000-tid-5790340178915489703-d0bf1a28-ced0-4475-890c-0836c456dacb-2353-17.c000.json", "/ecommerce/events/events-2020-07-03.json/hour=17/", "/ecommerce/events/events-2020-07-03.json/hour=17/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=17/_committed_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=17/_started_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=17/part-00000-tid-5790340178915489703-d0bf1a28-ced0-4475-890c-0836c456dacb-2353-18.c000.json", "/ecommerce/events/events-2020-07-03.json/hour=18/", "/ecommerce/events/events-2020-07-03.json/hour=18/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=18/_committed_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=18/_started_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=18/part-00000-tid-5790340178915489703-d0bf1a28-ced0-4475-890c-0836c456dacb-2353-19.c000.json", "/ecommerce/events/events-2020-07-03.json/hour=19/", "/ecommerce/events/events-2020-07-03.json/hour=19/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=19/_committed_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=19/_started_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=19/part-00000-tid-5790340178915489703-d0bf1a28-ced0-4475-890c-0836c456dacb-2353-20.c000.json", "/ecommerce/events/events-2020-07-03.json/hour=2/", "/ecommerce/events/events-2020-07-03.json/hour=2/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=2/_committed_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=2/_started_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=2/part-00000-tid-5790340178915489703-d0bf1a28-ced0-4475-890c-0836c456dacb-2353-3.c000.json", "/ecommerce/events/events-2020-07-03.json/hour=20/", "/ecommerce/events/events-2020-07-03.json/hour=20/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=20/_committed_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=20/_started_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=20/part-00000-tid-5790340178915489703-d0bf1a28-ced0-4475-890c-0836c456dacb-2353-21.c000.json", "/ecommerce/events/events-2020-07-03.json/hour=21/", "/ecommerce/events/events-2020-07-03.json/hour=21/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=21/_committed_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=21/_started_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=21/part-00000-tid-5790340178915489703-d0bf1a28-ced0-4475-890c-0836c456dacb-2353-22.c000.json", "/ecommerce/events/events-2020-07-03.json/hour=22/", "/ecommerce/events/events-2020-07-03.json/hour=22/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=22/_committed_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=22/_started_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=22/part-00000-tid-5790340178915489703-d0bf1a28-ced0-4475-890c-0836c456dacb-2353-23.c000.json", "/ecommerce/events/events-2020-07-03.json/hour=23/", "/ecommerce/events/events-2020-07-03.json/hour=23/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=23/_committed_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=23/_started_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=23/part-00000-tid-5790340178915489703-d0bf1a28-ced0-4475-890c-0836c456dacb-2353-24.c000.json", "/ecommerce/events/events-2020-07-03.json/hour=3/", "/ecommerce/events/events-2020-07-03.json/hour=3/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=3/_committed_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=3/_started_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=3/part-00000-tid-5790340178915489703-d0bf1a28-ced0-4475-890c-0836c456dacb-2353-4.c000.json", "/ecommerce/events/events-2020-07-03.json/hour=4/", "/ecommerce/events/events-2020-07-03.json/hour=4/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=4/_committed_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=4/_started_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=4/part-00000-tid-5790340178915489703-d0bf1a28-ced0-4475-890c-0836c456dacb-2353-5.c000.json", "/ecommerce/events/events-2020-07-03.json/hour=5/", "/ecommerce/events/events-2020-07-03.json/hour=5/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=5/_committed_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=5/_started_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=5/part-00000-tid-5790340178915489703-d0bf1a28-ced0-4475-890c-0836c456dacb-2353-6.c000.json", "/ecommerce/events/events-2020-07-03.json/hour=6/", "/ecommerce/events/events-2020-07-03.json/hour=6/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=6/_committed_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=6/_started_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=6/part-00000-tid-5790340178915489703-d0bf1a28-ced0-4475-890c-0836c456dacb-2353-7.c000.json", "/ecommerce/events/events-2020-07-03.json/hour=7/", "/ecommerce/events/events-2020-07-03.json/hour=7/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=7/_committed_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=7/_started_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=7/part-00000-tid-5790340178915489703-d0bf1a28-ced0-4475-890c-0836c456dacb-2353-8.c000.json", "/ecommerce/events/events-2020-07-03.json/hour=8/", "/ecommerce/events/events-2020-07-03.json/hour=8/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=8/_committed_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=8/_started_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=8/part-00000-tid-5790340178915489703-d0bf1a28-ced0-4475-890c-0836c456dacb-2353-9.c000.json", "/ecommerce/events/events-2020-07-03.json/hour=9/", "/ecommerce/events/events-2020-07-03.json/hour=9/_SUCCESS", "/ecommerce/events/events-2020-07-03.json/hour=9/_committed_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=9/_started_5790340178915489703", "/ecommerce/events/events-2020-07-03.json/hour=9/part-00000-tid-5790340178915489703-d0bf1a28-ced0-4475-890c-0836c456dacb-2353-10.c000.json", "/ecommerce/events/events-500k.json/", "/ecommerce/events/events-500k.json/_SUCCESS", "/ecommerce/events/events-500k.json/_committed_309888144738233288", "/ecommerce/events/events-500k.json/_started_309888144738233288", "/ecommerce/events/events-500k.json/part-00000-tid-309888144738233288-fab86c62-ff9f-4176-98c6-587f95ee9066-2365-1-c000.json", "/ecommerce/events/events.delta/", "/ecommerce/events/events.delta/_delta_log/", "/ecommerce/events/events.delta/_delta_log/.s3-optimization-0", "/ecommerce/events/events.delta/_delta_log/.s3-optimization-1", "/ecommerce/events/events.delta/_delta_log/.s3-optimization-2", "/ecommerce/events/events.delta/_delta_log/00000000000000000000.crc", "/ecommerce/events/events.delta/_delta_log/00000000000000000000.json", "/ecommerce/events/events.delta/part-00000-eb68ecaf-f8e1-4820-9513-24e158ed1e22-c000.snappy.parquet", "/ecommerce/events/events.delta/part-00001-e9be20a6-591a-4c06-9284-36d33f8bb378-c000.snappy.parquet", "/ecommerce/events/events.delta/part-00002-5793eed4-8dea-4287-abe1-a8ed30032f86-c000.snappy.parquet", "/ecommerce/events/events.delta/part-00003-3c9024f7-5419-45b5-873d-4756e510a797-c000.snappy.parquet", "/ecommerce/events/events.parquet/", "/ecommerce/events/events.parquet/_SUCCESS", "/ecommerce/events/events.parquet/_committed_5605450943866116740", "/ecommerce/events/events.parquet/_started_5605450943866116740", "/ecommerce/events/events.parquet/part-00000-tid-5605450943866116740-67d9bdb2-cc6b-4c16-b04c-d9ca9d63faa4-2309-1-c000.snappy.parquet", "/ecommerce/events/events.parquet/part-00001-tid-5605450943866116740-67d9bdb2-cc6b-4c16-b04c-d9ca9d63faa4-2310-1-c000.snappy.parquet", "/ecommerce/events/events.parquet/part-00002-tid-5605450943866116740-67d9bdb2-cc6b-4c16-b04c-d9ca9d63faa4-2311-1-c000.snappy.parquet", "/ecommerce/events/events.parquet/part-00003-tid-5605450943866116740-67d9bdb2-cc6b-4c16-b04c-d9ca9d63faa4-2312-1-c000.snappy.parquet", "/ecommerce/sales/", "/ecommerce/sales/sales.delta/", "/ecommerce/sales/sales.delta/_delta_log/", "/ecommerce/sales/sales.delta/_delta_log/.s3-optimization-0", "/ecommerce/sales/sales.delta/_delta_log/.s3-optimization-1", "/ecommerce/sales/sales.delta/_delta_log/.s3-optimization-2", "/ecommerce/sales/sales.delta/_delta_log/00000000000000000000.crc", "/ecommerce/sales/sales.delta/_delta_log/00000000000000000000.json", "/ecommerce/sales/sales.delta/part-00000-87b7cec6-2b1e-4c79-8be9-b41c3e248ebc-c000.snappy.parquet", "/ecommerce/sales/sales.delta/part-00001-34f65c3f-bf8e-417b-bb9d-4e9b93e78d8e-c000.snappy.parquet", "/ecommerce/sales/sales.delta/part-00002-b369681e-0911-44b9-9b6f-d821b9bac212-c000.snappy.parquet", "/ecommerce/sales/sales.delta/part-00003-a6ef8767-0a46-41f2-8f41-8b00207aa95d-c000.snappy.parquet", "/ecommerce/sales/sales.parquet/", "/ecommerce/sales/sales.parquet/_SUCCESS", "/ecommerce/sales/sales.parquet/_committed_3748607814555512113", "/ecommerce/sales/sales.parquet/_started_3748607814555512113", "/ecommerce/sales/sales.parquet/part-00000-tid-3748607814555512113-674b4353-084f-439c-843b-b751631dd899-2314-1-c000.snappy.parquet", "/ecommerce/sales/sales.parquet/part-00001-tid-3748607814555512113-674b4353-084f-439c-843b-b751631dd899-2315-1-c000.snappy.parquet", "/ecommerce/sales/sales.parquet/part-00002-tid-3748607814555512113-674b4353-084f-439c-843b-b751631dd899-2316-1-c000.snappy.parquet", "/ecommerce/sales/sales.parquet/part-00003-tid-3748607814555512113-674b4353-084f-439c-843b-b751631dd899-2317-1-c000.snappy.parquet", "/ecommerce/users/", "/ecommerce/users/users-500k.csv/", "/ecommerce/users/users-500k.csv/_SUCCESS", "/ecommerce/users/users-500k.csv/_committed_6798248775191304424", "/ecommerce/users/users-500k.csv/_started_6798248775191304424", "/ecommerce/users/users-500k.csv/part-00000-tid-6798248775191304424-0020915c-5cd2-4aae-8903-2d586d002073-2359-1-c000.csv", "/ecommerce/users/users.delta/", "/ecommerce/users/users.delta/_delta_log/", "/ecommerce/users/users.delta/_delta_log/.s3-optimization-0", "/ecommerce/users/users.delta/_delta_log/.s3-optimization-1", "/ecommerce/users/users.delta/_delta_log/.s3-optimization-2", "/ecommerce/users/users.delta/_delta_log/00000000000000000000.crc", "/ecommerce/users/users.delta/_delta_log/00000000000000000000.json", "/ecommerce/users/users.delta/part-00000-c6c6ef40-dcdc-4f2e-937f-c4665668f9d8-c000.snappy.parquet", "/ecommerce/users/users.delta/part-00001-f4e8447a-9125-4629-bd4e-d14037d2cd55-c000.snappy.parquet", "/ecommerce/users/users.delta/part-00002-29c92a41-3ade-4d2f-b54e-2d08891a6b29-c000.snappy.parquet", "/ecommerce/users/users.delta/part-00003-2c30ce17-b31b-41eb-8257-646d795032e9-c000.snappy.parquet", "/people/", "/people/README.md", "/people/people-with-dups.txt", "/products/", "/products/README.md", "/products/products.csv/", "/products/products.csv/_SUCCESS", "/products/products.csv/_committed_1663954264736839188", "/products/products.csv/_started_1663954264736839188", "/products/products.csv/part-00000-tid-1663954264736839188-daf30e86-5967-4173-b9ae-d1481d3506db-2367-1-c000.csv", "/products/products.csv/part-00001-tid-1663954264736839188-daf30e86-5967-4173-b9ae-d1481d3506db-2368-1-c000.csv", "/products/products.csv/part-00002-tid-1663954264736839188-daf30e86-5967-4173-b9ae-d1481d3506db-2369-1-c000.csv", "/products/products.csv/part-00003-tid-1663954264736839188-daf30e86-5967-4173-b9ae-d1481d3506db-2370-1-c000.csv", "/products/products.delta/", "/products/products.delta/_delta_log/", "/products/products.delta/_delta_log/.s3-optimization-0", "/products/products.delta/_delta_log/.s3-optimization-1", "/products/products.delta/_delta_log/.s3-optimization-2", "/products/products.delta/_delta_log/00000000000000000000.crc", "/products/products.delta/_delta_log/00000000000000000000.json", "/products/products.delta/part-00000-8205eeb7-4264-4a62-afdb-b7f04ce8bc01-c000.snappy.parquet", "/products/products.delta/part-00001-747065ed-b76b-4773-a399-b7f69f671036-c000.snappy.parquet", "/products/products.delta/part-00002-e7e42eba-78db-4c31-97d7-de67c8c8eaca-c000.snappy.parquet", "/products/products.delta/part-00003-27fae240-3d2b-427f-b2c9-c4999db0485f-c000.snappy.parquet"]