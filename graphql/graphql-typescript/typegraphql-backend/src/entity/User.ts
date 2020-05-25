import { Entity, PrimaryGeneratedColumn, Column } from "typeorm";
import { Field, ObjectType, ID } from "type-graphql";

@ObjectType()
@Entity()
export class User {
  @Field(() => ID)
  @PrimaryGeneratedColumn()
  id: number;

  @Field()
  @Column()
  firstName: string;

  @Field()
  @Column("text", { unique: true })
  email: string;

  @Column()
  password: string;
}
