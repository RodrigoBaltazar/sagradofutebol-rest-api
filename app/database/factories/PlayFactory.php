<?php

namespace Database\Factories;

use App\Models\Play;
use Illuminate\Database\Eloquent\Factories\Factory;

class PlayFactory extends Factory
{
    /**
     * The name of the factory's corresponding model.
     *
     * @var string
     */
    protected $model = Play::class;

    /**
     * Define the model's default state.
     *
     * @return array
     */
    public function definition()
    {
        return [
            'title' => $this->faker->text(10),
            'path' => $this->faker->text(10)
        ];
    }
}
