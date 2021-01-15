<?php

namespace Database\Seeders;

use Illuminate\Database\Seeder;

class PlaysTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        Plays::truncate();

        $faker = \Faker\Factory::create();

        // And now, let's create a few articles in our database:
        for ($i = 0; $i < 10; $i++) {
            Plays::create([
                'title' => $faker->sentence,
                'path' => $faker->paragraph,
            ]);
        }
    }
}
