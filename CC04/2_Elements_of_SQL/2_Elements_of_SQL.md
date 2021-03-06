### Offset

```
select name, birthdate from animals order by name limit 10 offset 20;
```

- Limit will limit the results
- offset will skip the number of rows from which the result will start.

### group by
The group by clause is only used with aggregations, such as max or sum.

```
-- Write a query that returns all the species in the zoo, and how many
-- animals of each species there are, sorted with the most populous
-- species at the top.
--
-- The result should have two columns:  species and number.
--
-- The animals table has columns (name, species, birthdate) for each animal.

select species, count(species) a from animals group by species order by a desc;
```

### Where and Having
- Where is a restriction on the source table.
- Having is a restriction on the result ... after aggregation.

```
select food, count(*) as num
    from animals join diet
    on animals.species = diet.species
    group by food
    having num = 1;
```
## Redo
More Join Practice